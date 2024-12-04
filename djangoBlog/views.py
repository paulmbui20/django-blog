from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from accounts.models import CustomUser
from blog.models import BlogPost, Category

from django.contrib.auth import get_user_model

def index(request):
    recent_posts = BlogPost.objects.filter(status='published').order_by('-created_at')[:5]
    posts = BlogPost.objects.filter(status='published').order_by('-created_at') [:8]
    categories = Category.objects.all()[:4]
    context = { 'recent_posts': recent_posts, 'categories': categories, 'posts': posts}
    return render(request, 'index.html', context)


CustomUser = get_user_model()
def author(request, slug):
    # Retrieve the author by username (slug)
    author = get_object_or_404(CustomUser, username=slug)

    # Filter blog posts by the author
    posts = BlogPost.objects.filter(author=author)

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
                'bio': author.bio,  # Assuming bio is in the profile
                'website': author.website,  # Assuming website is in the profile
                'image': author.image,  # Assuming picture is in the profile
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
