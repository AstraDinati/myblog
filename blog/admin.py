from django import forms
from django.contrib import admin
from .models import Post, Tag


class TagInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        tags = [
            form.cleaned_data.get("tag")
            for form in self.forms
            if form.cleaned_data.get("tag")
        ]
        if len(tags) != len(set(tags)):
            raise forms.ValidationError(
                "Each tag should only be selected once per post."
            )


class TagInline(admin.TabularInline):
    model = Post.tags.through
    formset = TagInlineFormSet


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [TagInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
