import json
import os

from django.contrib.admin.views.decorators import staff_member_required
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials

from googleapiclient.discovery import build

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import BlogPostForm, ContactForm
from .models import BlogPost, Category

from django.contrib.auth.decorators import user_passes_test

def BlogPostListView(request):
    posts = BlogPost.objects.filter(status='published')  # Filter posts by status 'published'
    categories = Category.objects.all()
    years = BlogPost.objects.dates('created_at', 'year')  # Get unique years for archive links
    recent_posts = BlogPost.objects.filter(status='published').order_by('-created_at')[:5]  # Last 5 published posts

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
        'recent_posts': recent_posts,
        'page_obj': page_obj,

    }
    return render(request, 'blogpost_list.html', context)

def BlogPostDetailView(request, slug):
    # Fetch the blog post by slug
    post = get_object_or_404(BlogPost, slug=slug)

    if post.status != 'published':
        return render(request, 'unpublished.html')  # Render a placeholder for unpublished posts

    # Additional data
    categories = Category.objects.all()
    recent_posts = BlogPost.objects.filter(status='published').order_by('-created_at')[:5]  # Last 5 published posts

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
    }

    # Render the detail template
    return render(request, 'blogpost_detail.html', context)

def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = BlogPost.objects.filter(categories=category,status='published')  # Only show published posts
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
        results = BlogPost.objects.filter(title__icontains=query, status='published').values('id', 'title', 'slug', 'updated_at')
        return JsonResponse(list(results), safe=False)
    return JsonResponse([], safe=False)  # Return an empty list if no query


@login_required
def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the author as the logged-in user
            post.status = 'pending'  # Set default status to 'pending'
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
        if post.author != request.user.is_superuser:
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
VIEW_ID = os.getenv('GOOGLE_ANALYTICS_PROPERTY_ID')

def get_google_analytics_data():
    # Create credentials from the JSON dictionary
    credentials = Credentials.from_service_account_info(GOOGLE_CREDENTIALS)

    # Build the Analytics API client
    analytics = build('analyticsreporting', 'v4', credentials=credentials)

    # Fetch analytics data
    response = analytics.reports().batchGet(
        body={
            'reportRequests': [
                {
                    'viewId': VIEW_ID,
                    'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                    'metrics': [{'expression': 'ga:sessions'}, {'expression': 'ga:pageviews'}],
                    'dimensions': [{'name': 'ga:pagePath'}],
                }
            ]
        }
    ).execute()
    return response

@staff_member_required
def analytics_dashboard(request):
    # Get the Google Analytics data
    raw_data = get_google_analytics_data()

    # Extract rows from the API response
    rows = []
    for row in raw_data.get('rows', []):
        rows.append({
            'page': row['dimensionValues'][0]['value'],
            'sessions': row['metricValues'][0]['value'],
            'pageviews': row['metricValues'][1]['value'],
        })

    # Pass the rows to the template
    return render(request, 'analytics_dashboard.html', {'rows': rows})
