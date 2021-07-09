from django import forms
from django.contrib.auth.models import User
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['author','title','content','post_image','blog_views','category']
        widgets = {
            'author': forms.TextInput(attrs={'type': 'hidden'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'blog_views': forms.TextInput(attrs={'type': 'hidden'}),
            'content': forms.Textarea(attrs={'class': 'form-control' }),
            'category': forms.Select(attrs={'class': 'form-control', }),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content','Full_Name','email']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control',
                                              'style':'height:80px;'}),
            'Full_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
class EditPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ['author', 'title', 'content', 'post_image', 'blog_views', 'category']
        widgets = {
            'author': forms.TextInput(attrs={'type': 'hidden'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'blog_views': forms.TextInput(attrs={'type': 'hidden'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control', }),
        }
class SuggestForm(forms.ModelForm):
    class Meta:
        model=Suggestion
        fields=['name','email','message']
        widgets = {
              'name':forms.TextInput(attrs={'class':'form-control'}),
              'email':forms.TextInput(attrs={'class':'form-control'}),
             'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'your suggestion here!',})
        }

