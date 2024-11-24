from django import forms
from .models import BlogPost, Category
from dal import autocomplete

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']



class BlogPostForm(forms.ModelForm):
    content = forms.CharField()
    class Meta:
        model = BlogPost
        fields = ['title', 'featured_image', 'content', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'featured_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'categories': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }
