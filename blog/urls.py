# blog/urls.py
from django.urls import path
from .views import post_list, post_detail, tag_filter, about, test


urlpatterns = [
    path("", post_list, name="post_list"),
    path("post/<int:pk>/", post_detail, name="post_detail"),
    path("tag-filter/", tag_filter, name="tag_filter"),
    path("about", about, name="about"),
    path("test", test, name="test"),
]
