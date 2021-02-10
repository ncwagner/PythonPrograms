from django import forms
from .models import Post


class PostList(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'created_date', 'published_date')
