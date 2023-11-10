# forms.py

from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    tags = forms.CharField(help_text="Enter tags separated by commas")

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
