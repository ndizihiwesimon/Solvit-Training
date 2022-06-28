from random import choices
from django import forms
from django.contrib.auth import get_user_model
from blog.models import Post
User=get_user_model()
class UserRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'
        
class BlogForm(forms.ModelForm):

    title = forms.CharField(max_length=255, required=True, widget=forms.widgets.Input(attrs={'class': 'form-control', 'placeholder': 'Blog title'}))
    content = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'class': 'form-control', 'placeholder': 'Blog content'}))
    slug = forms.CharField(max_length=255, required=True, widget=forms.widgets.Input(attrs={'class': 'form-control', 'placeholder': 'Blog slug'}))
    # author = forms.CharField(max_length=255, required=True, widget=forms.widgets.Select(attrs={'class': 'form-control'}))
    # status = forms.CharField(max_length=255, required=True, widget=forms.widgets.Select(attrs={'class': 'form-control'})
    class Meta:
        model=Post
        fields='__all__'
        