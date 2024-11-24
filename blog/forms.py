from django import forms
from .models import BlogPost, Category
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
