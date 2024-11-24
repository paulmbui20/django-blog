
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from blog.models import BlogPost
from .forms import CustomUserCreationForm, CustomAuthenticationForm



def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# def login_view(request):
#     if request.method == "POST":
#         form = CustomAuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username_or_email = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(
#                 request,
#                 username=username_or_email,
#                 password=password
#             )
#             if user:
#                 login(request, user)
#                 return redirect('account')
#     else:
#         form = CustomAuthenticationForm()
#     return render(request, 'registration/login.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Authenticate with username
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('account')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Error in the form. Please correct it.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def account(request):
    if request.user.is_superuser:
        posts = BlogPost.objects.all()
    else:
        posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'registration/account.html', {'posts': posts})
