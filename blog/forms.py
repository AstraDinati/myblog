# blog/forms.py
from django import forms
from .models import Post, Tag


class PostForm(forms.ModelForm):
    tags = forms.CharField(help_text="Enter tags separated by commas")

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

    def save(self, commit=True):
        post = super().save(commit=False)
        tags = [tag.strip() for tag in self.cleaned_data["tags"].split(",")]
        post.set_tags(tags)

        if commit:
            post.save()
        return post
