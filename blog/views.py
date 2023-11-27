# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    active_link = "post_list"
    posts = Post.objects.all().order_by("-pub_date")
    tags = Tag.objects.all().order_by("name")

    # Добавляем пагинацию
    paginator = Paginator(posts, 10)  # Показывать 10 постов на каждой странице
    page = request.GET.get("page")

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(
        request,
        "blog/post_list.html",
        {"posts": posts, "tags": tags, "active_link": active_link},
    )


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


def about(request):
    active_link = "about"
    return render(request, "blog/about.html", {"active_link": active_link})


def test(request):
    return render(request, "blog/test.html")


def tag_filter(request):
    tag_name = request.GET.get("tag")
    action = request.GET.get("action")
    selected_tags = request.session.get("selected_tags", [])
    is_tag_container_show = True

    if tag_name:
        if action == "add" and tag_name not in selected_tags:
            selected_tags.append(tag_name)
        elif action == "remove" and tag_name in selected_tags:
            selected_tags.remove(tag_name)
        else:
            # Если тег уже выбран, сбросить его
            if tag_name in selected_tags:
                selected_tags.remove(tag_name)
            else:
                # Если тег не выбран, добавить его к выбранным тегам
                selected_tags.append(tag_name)

    posts = Post.objects.all().order_by("-pub_date")

    for tag in selected_tags:
        posts = posts.filter(tags__name=tag)

    if "selected_tags" in request.GET:
        request.session["selected_tags"] = []
        return redirect(request.path)

    paginator = Paginator(posts, 10)
    page = request.GET.get("page")

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    tags = Tag.objects.all().order_by("name")

    request.session["selected_tags"] = selected_tags

    if selected_tags == []:
        is_tag_container_show = False

    return render(
        request,
        "blog/post_list.html",
        {
            "posts": posts,
            "tags": tags,
            "selected_tags": selected_tags,
            "is_tag_container_show": is_tag_container_show,
        },
    )
