from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import BlogPostForm
from .models import BlogPost, Category
from django.http import JsonResponse, HttpResponseRedirect


def BlogPostListView(request):
    posts = BlogPost.objects.all()
    categories = Category.objects.all()
    years = BlogPost.objects.dates('created_at', 'year')  # Get unique years for archive links
    recent_posts = BlogPost.objects.all().order_by('-created_at')[:5]  # Last 5 posts

    # tags = tags.objects.all()
    breadcrumbs = [
        {'url': '/', 'name': 'Home'},
        {'url': '/posts/', 'name': 'Blog'}
    ]
    context = {
        'posts': posts,
        'categories': categories,
        # 'tags': tags,
        'breadcrumbs': breadcrumbs,  # Pass breadcrumbs to the template
        'years': years,
        'recent_posts': recent_posts,  # Last 5 posts

    }
    return render(request, 'blogpost_list.html', context)

def BlogPostDetailView(request, slug):
    # Fetch the blog post by slug
    post = get_object_or_404(BlogPost, slug=slug)

    # Additional data
    categories = Category.objects.all()
    recent_posts = BlogPost.objects.all().order_by('-created_at')[:5]  # Last 5 posts
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
    }

    # Render the detail template
    return render(request, 'blogpost_detail.html', context)

def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = BlogPost.objects.filter(categories=category)
    recent_posts = BlogPost.objects.all().order_by('-created_at')[:5]  # Last 5 posts
    breadcrumbs = [
        {'url': '/', 'name': 'Home'},
        {'url': '/posts/', 'name': 'Blog'},
    ]
    context = {
        'category': category,
        'recent_posts': recent_posts,
        'posts': posts,
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'category_detail.html', context)

def search_posts(request):
    query = request.GET.get('q', '').strip()
    if query:
        results = BlogPost.objects.filter(title__icontains=query).values('id', 'title', 'slug')
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

