# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post, Tag


def post_list(request):
    posts = Post.objects.all().order_by("-pub_date")
    tags = Tag.get_all_tags()
    return render(request, "blog/post_list.html", {"posts": posts, "tags": tags})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


def tag_filter(request):
    tag_name = request.GET.get("tag")
    posts = Post.objects.filter(tags__name=tag_name) if tag_name else Post.objects.all()
    tags = Tag.get_all_tags()

    return render(
        request,
        "blog/post_list.html",
        {"posts": posts, "tags": tags, "selected_tag": tag_name},
    )
