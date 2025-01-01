
import os

from django.utils import timezone

from django.contrib.admin.views.decorators import staff_member_required
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials

from googleapiclient.discovery import build
from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import BlogPostForm, ContactForm, CategoryForm, CommentForm
from .models import BlogPost, Category, AnalyticsData, Comment

from django.contrib.auth.decorators import user_passes_test

def BlogPostListView(request):
    posts = BlogPost.objects.filter(status='published').order_by('-created_at')  # Filter posts by status 'published'
    categories = Category.objects.all()
    years = BlogPost.objects.dates('created_at', 'year')  # Get unique years for archive links

    paginator = Paginator(posts, 16)  #pagination to show 16 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    breadcrumbs = [
        {'url': '/', 'name': 'Home'},
        {'url': '/posts/', 'name': 'Blog'}
    ]
    context = {
        'posts': posts,
        'categories': categories,
        'breadcrumbs': breadcrumbs,
        'years': years,
        'page_obj': page_obj,

    }
    return render(request, 'blogpost_list.html', context)

def BlogPostDetailView(request, slug):
    # Fetch the blog post by slug
    post = get_object_or_404(BlogPost, slug=slug)
    form = CommentForm()
    if post.status != 'published':
        return render(request, 'unpublished.html')  # Render a placeholder for unpublished posts

    # Additional data
    categories = Category.objects.all()
    recent_posts = BlogPost.objects.filter(status='published').order_by('-created_at')[:5]  # Last 5 published posts
    comments = Comment.objects.filter(blog_post=post).order_by('-created_at')
    comments_count = comments.count()
    # Get related posts based on the category
    related_posts = BlogPost.objects.filter(
        categories=post.categories,
        status='published'
    ).exclude(id=post.id)[:4]  # Exclude the current post and limit to 5

    breadcrumbs = [
        {'url': '/', 'name': 'Home'},
        {'url': '/posts/', 'name': 'Blog'},
        {'url': f'/posts/{post.slug}/', 'name': post.title}
    ]

    # Context to pass to the template
    context = {
        'post': post,  # Single blog post for detail
        'categories': categories,
        'breadcrumbs': breadcrumbs,
        'recent_posts': recent_posts,
        'related_posts': related_posts,  # Add related posts to the context
        'form': form,
        'comments': comments,
        'comments_count': comments_count,
    }

    # Render the detail template
    return render(request, 'blogpost_detail.html', context)

def commentform(request, slug):
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Comment successfully saved')
                return redirect('blogpost_detail', slug=slug)
            else:
                messages.error(request, 'Please check your input')
                return redirect('blogpost_detail', slug=slug)
        else:
            messages.error(request, 'Error')

def deletecomment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_slug = request.POST.get('post_slug')
    if request.user.is_superuser:
        if request.method == 'POST':
            comment.delete()
            messages.success(request, 'Comment successfully deleted')
            return redirect('blogpost_detail', slug=post_slug)
        else:
            messages.error(request, 'Invalid request')
            return redirect('blogpost_detail', slug=post_slug)
    else:
        messages.error(request, 'You are not authorized to perform this action')
        return redirect('blogpost_detail', slug=post_slug)
def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = BlogPost.objects.filter(categories=category,status='published').order_by('-created_at')  # Only show published posts
    recent_posts = BlogPost.objects.filter(status='published').order_by('-created_at')[:5]  # Last 5 published posts

    paginator = Paginator(posts, 16)  #pagination to show 16 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    breadcrumbs = [
        {'url': '/', 'name': 'Home'},
        {'url': '/posts/', 'name': 'Blog'},
    ]
    context = {
        'category': category,
        'recent_posts': recent_posts,
        'posts': posts,
        'breadcrumbs': breadcrumbs,
        'page_obj': page_obj,
    }
    return render(request, 'category_detail.html', context)

def search_posts(request):
    query = request.GET.get('q', '').strip()
    if query:
        results = BlogPost.objects.filter(title__icontains=query, status='published').values('id', 'title', 'slug', 'updated_at')[:5]
        return JsonResponse(list(results), safe=False)
    return JsonResponse([], safe=False)  # Return an empty list if no query

@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category_name = form.cleaned_data['name']
            category_image = form.cleaned_data['categoryImage']
            category_description = form.cleaned_data['description']
            category = Category(name=category_name, categoryImage=category_image, description=category_description)
            category.save()
            messages.success(request, 'Category Added')
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})


@staff_member_required
def edit_category(request, slug):
    if request.method == 'POST':
        category = get_object_or_404(Category, slug=slug)
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category Updated Successfully')
            return redirect('category_list')
    else:
        form = CategoryForm(instance=Category.objects.get(slug=slug))
    return render(request, 'edit_category.html', {'form': form})


@login_required
def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the author as the logged-in user
            if post.author.is_superuser:
                post.status = 'published'  # Set default status to 'pending'
            else:
                post.status = 'pending'
            post.save()
            form.save_m2m()  # Save the many-to-many data
            messages.success(request, 'Your post has been submitted for review.')
            return redirect('account')  # Redirect to the account page
    else:
        form = BlogPostForm()

    return render(request, 'add_post.html', {'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    # Ensure only the author or a superuser can edit the post
    if post.author != request.user and not request.user.is_superuser:
        messages.error(request, "You don't have permission to edit this post.")
        return redirect('account')

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if request.user.is_superuser:
            post.status = 'published'
        elif post.author != request.user.is_superuser:
            post.status = 'pending'

        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully.")
            return redirect('account')
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    # Ensure only the author or a superuser can delete the post
    if post.author != request.user and not request.user.is_superuser:
        messages.error(request, "You don't have permission to delete this post.")
        return redirect('account')

    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return HttpResponseRedirect(reverse('account'))

    return render(request, 'registration/account.html', {'post': post})


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def update_post_status(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        new_status = request.POST.get('new_status')
        try:
            post = BlogPost.objects.get(id=post_id)
            post.status = new_status
            post.save()
            return JsonResponse({'message': 'Status updated successfully!'}, status=200)
        except BlogPost.DoesNotExist:
            return JsonResponse({'message': 'Post not found!'}, status=404)
    return JsonResponse({'message': 'Invalid request method!'}, status=400)


def contactform(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success":True ,"message": "Message sent successfully!"}, status=200)
        else:
            return JsonResponse({"success": False, "message": "Invalid field input, check input."}, status=400)
    else:
        return JsonResponse({"success": False, "message": "Invalid request method!"}, status=500)

def contact(request):
    return render(request, 'contact.html', {'form': ContactForm()})


# Load environment variables from .env
load_dotenv()


# Create a dictionary for credentials from environment variables
GOOGLE_CREDENTIALS = {
    "type": os.getenv("GOOGLE_TYPE"),
    "project_id": os.getenv("GOOGLE_PROJECT_ID"),
    "private_key_id": os.getenv("GOOGLE_PRIVATE_KEY_ID"),
    "private_key": os.getenv("GOOGLE_PRIVATE_KEY").replace('\\n', '\n'),  # Fix newlines
    "client_email": os.getenv("GOOGLE_CLIENT_EMAIL"),
    "client_id": os.getenv("GOOGLE_CLIENT_ID"),
    "auth_uri": os.getenv("GOOGLE_AUTH_URI"),
    "token_uri": os.getenv("GOOGLE_TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("GOOGLE_AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("GOOGLE_CLIENT_X509_CERT_URL"),
}
# Your Google Analytics View ID (store this in the .env too if needed)
property_id = os.getenv('GOOGLE_ANALYTICS_PROPERTY_ID')

def fetch_and_store_google_analytics_data():
    # Create credentials from the JSON dictionary
    credentials = Credentials.from_service_account_info({
        "type": os.getenv("GOOGLE_TYPE"),
        "project_id": os.getenv("GOOGLE_PROJECT_ID"),
        "private_key_id": os.getenv("GOOGLE_PRIVATE_KEY_ID"),
        "private_key": os.getenv("GOOGLE_PRIVATE_KEY").replace('\\n', '\n'),
        "client_email": os.getenv("GOOGLE_CLIENT_EMAIL"),
        "client_id": os.getenv("GOOGLE_CLIENT_ID"),
        "auth_uri": os.getenv("GOOGLE_AUTH_URI"),
        "token_uri": os.getenv("GOOGLE_TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("GOOGLE_AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": os.getenv("GOOGLE_CLIENT_X509_CERT_URL"),
    })

    # Build the Analytics API client
    analytics = build('analyticsdata', 'v1beta', credentials=credentials)

    # Use your GA4 property ID
    property_id = os.getenv("GOOGLE_ANALYTICS_PROPERTY_ID")

    # Fetch data using the GA4 Data API
    response = analytics.properties().runReport(
        property=f"properties/{property_id}",
        body={
            "dateRanges": [{"startDate": "7daysAgo", "endDate": "today"}],
            "dimensions": [{"name": "pagePath"}],
            "metrics": [{"name": "sessions"}, {"name": "screenPageViews"}],
        },
    ).execute()

    # Clear old data (optional: keep a historical record if desired)
    AnalyticsData.objects.all().delete()

    # Process and store new data
    for row in response.get('rows', []):
        page_path = row['dimensionValues'][0]['value']
        sessions = int(row['metricValues'][0]['value'])
        pageviews = int(row['metricValues'][1]['value'])
        absolute_url = f"http://127.0.0.1{page_path}"  # Replace with your domain

        AnalyticsData.objects.create(
            page_path=page_path,
            sessions=sessions,
            pageviews=pageviews,
            absolute_url=absolute_url,
        )
@staff_member_required
def analytics_dashboard(request):
    # Check if the last update is more than 24 hours ago
    last_entry = AnalyticsData.objects.order_by('-last_updated').first()
    if not last_entry or last_entry.last_updated < timezone.now() - timedelta(days=1):
        fetch_and_store_google_analytics_data()  # Fetch new data if stale

    # Retrieve data from the database
    rows = AnalyticsData.objects.all()
    return render(request, 'analytics_dashboard.html', {'rows': rows})
