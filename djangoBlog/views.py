from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from accounts.models import CustomUser
from blog.models import BlogPost, Category

from django.contrib.auth import get_user_model

def index(request):
    recent_posts = BlogPost.objects.filter(status='published').order_by('-created_at')[:5]
    posts = BlogPost.objects.filter(status='published').order_by('-created_at') [:12]
    categories = Category.objects.all()[:4]
    context = { 'recent_posts': recent_posts, 'categories': categories, 'posts': posts}
    return render(request, 'index.html', context)


def author(request, slug):
    # Retrieve the author by username (slug)
    author = get_object_or_404(CustomUser, username=slug)

    # Filter blog posts by the author
    posts = BlogPost.objects.filter(author=author).order_by('-created_at')

    # Custom breadcrumbs
    breadcrumbs = [
        {'name': 'Authors', 'url': '/authors/'},
        {'name': author.username, 'url': f'/authors/{author.username}/'},
    ]

    context = {
        'author': author,
        'posts': posts,
        'breadcrumbs': breadcrumbs,

    }
    return render(request, 'author.html', context)


def authors_list_view(request):
    authors = CustomUser.objects.all()
    author_details = []


    for author in authors:
        author_posts = BlogPost.objects.filter(author=author, status='published').count()
        if author_posts >= 1:  # Only list authors with more 1 or more  published post
            author_details.append({
                'username': author.username,
                'first_name': author.first_name,
                'last_name': author.last_name,
                'bio': author.bio,
                'website': author.website,
                'image': author.image,
                'post_count': author_posts
            })
    paginator = Paginator(authors, 16)  #pagination to show 16 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    breadcrumbs = [
        {'name': 'Home', 'url': '/'},
        {'name': 'Articles', 'url': '/posts/'},
        {'name': 'Authors', 'url': '/authors/'},
    ]
    context = {
        'author_details': author_details,
        'breadcrumbs': breadcrumbs,
        'page_obj': page_obj,
    }
    return render(request, 'authors_list.html', context)

def category_list_view(request):
    categories = Category.objects.all()
    category_details = []

    for category in categories:
        post_count = BlogPost.objects.filter(categories=category, status='published').count()
        if post_count > 0:  # Only include categories with at least one published post
            category_details.append({
                'name': category.name,
                'slug': category.slug,
                'post_count': post_count,
                'description': category.description,
                'category_image': category.categoryImage,
            })
    paginator = Paginator(categories, 16)  #pagination to show 16 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    breadcrumbs = [
        {'name': 'Home', 'url': '/'},
        {'name': 'Articles', 'url': '/posts/'},
        {'name': 'Categories', 'url': '/categories/'},

    ]
    context = {
        'category_details': category_details,
        'breadcrumbs': breadcrumbs,
        'page_obj': page_obj,
    }
    return render(request, 'category_list.html', context)

def search (request):
    query = request.GET.get('q', '')
    if query:
        results = (BlogPost.objects.filter(
            Q(title__icontains=query) , status='published')
                   .order_by('-created_at'))
        paginator = Paginator(results, 16)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
            'query': query,
        }
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')