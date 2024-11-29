from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'name@example.com',
        'id': 'floatingInput',
    }))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("This email is already taken.")
        return email

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'johndoe',
        'id': 'floatingUsername',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'id': 'floatingPassword',
        'label': 'Password',
    }), label='Password')

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
        'id': 'floatingPasswordC',
        'label': 'Confirm Password',
    }), label="Confirm Password")

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'username',
        'id': 'floatingInput',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'id': 'floatingPassword',
    }))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'bio', 'website', 'gender'  ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name',
                'id': 'floatingFirstName',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name',
                'id': 'floatingLastName',
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'id': 'floatingUsername',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'id': 'floatingEmail',
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone',
                'id': 'floatingPhone',
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Bio',
                'id': 'floatingBio',
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Website',
                'id': 'floatingWebsite',
            }),
            'gender': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Gender',
                'id': 'floatingGender',
            })
        }