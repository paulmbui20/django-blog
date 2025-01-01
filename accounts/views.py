import os

from django.contrib.auth import update_session_auth_hash, login, authenticate, get_backends
from django.http import JsonResponse

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from blog.models import BlogPost, Contact
from .forms import CustomUserCreationForm, CustomAuthenticationForm, ProfileForm

import jwt
from datetime import datetime, timedelta
from django.conf import settings

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            backend = get_backends()[0]  # Use the first backend or specify the index
            user.backend = f"{backend.__module__}.{backend.__class__.__name__}"
            messages.success(request, "Account created successfully")
            login(request, user)
            return redirect('account')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user is not None:
                backend = get_backends()[0]
                user.backend = f"{backend.__module__}.{backend.__class__.__name__}"
                login(request, user)
                messages.success(request, "Logged in successfully")
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
    messages.success(request, "Logged out successfully")
    return redirect('login')


@login_required
def account(request):
    if request.user.is_superuser:
        posts = BlogPost.objects.all()
    else:
        posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'registration/account.html', {'posts': posts})



@login_required
def update_password(request):
    if request.method == "POST":
        old_password = request.POST.get("password")
        new_password = request.POST.get("newpassword")
        confirm_password = request.POST.get("confirm_password")

        if new_password != confirm_password:
            return JsonResponse({"success": False, "message": "Passwords do not match."})

        if not request.user.check_password(old_password):
            return JsonResponse({"success": False, "message": "Old password is incorrect."})

        request.user.set_password(new_password)
        request.user.save()

        # Keep the user logged in after changing the password
        update_session_auth_hash(request, request.user)

        return JsonResponse({"success": True, "message": "Password updated successfully."})

    return JsonResponse({"success": False, "message": "Invalid request."})


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
            form = ProfileForm(instance=user)
    else:
        form = ProfileForm(instance=user)

    return render(request, 'registration/profile.html', {
        'user': user,
        'form': form
    })

@login_required
def update_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        user = request.user
        image = request.FILES['image']
        user.image = image
        user.save()
        return JsonResponse({'success': True, 'message': 'Profile image updated successfully.'})
    return JsonResponse({'success': False, 'message': 'Invalid request or no image provided.'}, status=400)

@login_required
def delete_image(request):
    if request.method == 'POST':
        user = request.user
        if user.image:  # Check if the user has an image
            try:
                # Remove the file from storage
                if os.path.isfile(user.image.path):
                    os.remove(user.image.path)
                # Clear the image field in the database
                user.image = None
                user.save()
                return JsonResponse({'success': True, 'message': 'Profile image deleted successfully.'})
            except Exception as e:
                return JsonResponse({'success': False, 'message': f'Error deleting image: {str(e)}'}, status=500)
        else:
            return JsonResponse({'success': False, 'message': 'No profile image to delete.'}, status=400)
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)


# Function to create JWT token
def create_jwt_token(user):
    payload = {
        'user_id': user.id, 'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(), # Issued at
        }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token
# Function to decode JWT token
def decode_jwt_token(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None
    # Token has expired
    except jwt.InvalidTokenError:
        return None # Invalid token

@login_required
def queries(request):
    if request.user.is_superuser:
        contact_queries = Contact.objects.all()
        context = {
            'contact_queries': contact_queries
        }
        return render(request, 'queries.html', context)
    else:
        messages.error(request, "You are not authorized to access this page.")
        return redirect('login')

@login_required
def delete_contact_query(request):
    if request.method == 'POST':
        pk = request.POST.get('id')
        contact = get_object_or_404(Contact, pk=pk)
        if request.user.is_superuser:
            contact.delete()
            # messages.success(request, 'Contact query deleted successfully.')
            return JsonResponse({'success': True, 'message': 'Contact query deleted successfully.'})
        else:
            return JsonResponse({'success': False, 'message': 'You are not authorized to perform this action.'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request.'})
