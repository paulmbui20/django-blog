from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from .models import BlogPost, Category, Contact


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'categoryImage']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'categoryImage':forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }



class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'featured_image', 'content', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'featured_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'categories': forms.Select(attrs={'class': 'form-select'}),
            "content": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="default"
            )
        }
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['FirstName', 'LastName', 'email', 'phone', 'message']
        widgets = {
            'FirstName': forms.TextInput(attrs={
                'class': 'form-control',
                'label': 'First Name',
                'placeholder': 'First Name',
                'id': 'firstname',
            }),
            'LastName': forms.TextInput(attrs={
                'class': 'form-control',
                'label': 'Last Name',
                'placeholder': 'Enter your Last Name',
                'id': 'lastname',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'label': 'Email',
                 'placeholder': 'Enter your Email',
                'id': 'email',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'label': 'Phone',
                'placeholder': 'Enter your Phone',
                'id': 'phone',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'label': 'Message',
                'placeholder': 'Enter your Message',
                'id': 'message',
            }),
        }