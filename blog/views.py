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
    action = request.GET.get("action")
    selected_tags = request.session.get("selected_tags", [])

    if tag_name:
        if action == "add" and tag_name not in selected_tags:
            selected_tags.append(tag_name)
        elif action == "remove" and tag_name in selected_tags:
            selected_tags.remove(tag_name)
        else:
            selected_tags = [tag_name]

    posts = Post.objects.all()

    if selected_tags:
        posts = posts.filter(tags__name__in=selected_tags)

    tags = Tag.get_all_tags()

    request.session["selected_tags"] = selected_tags

    return render(
        request,
        "blog/post_list.html",
        {"posts": posts, "tags": tags, "selected_tags": selected_tags},
    )
