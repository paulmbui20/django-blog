from django import forms
from .models import BlogPost, Category, Contact
from froala_editor.widgets import FroalaEditor

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']



class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=FroalaEditor)
    class Meta:
        model = BlogPost
        fields = ['title', 'featured_image', 'content', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'featured_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'categories': forms.Select(attrs={'class': 'form-select'}),
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