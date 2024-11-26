from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import CustomUser
from blog.models import BlogPost

from django.contrib.auth import get_user_model

def index(request):
    return render(request, 'index.html')

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