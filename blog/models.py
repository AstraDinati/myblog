# models.py
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    photo = models.ImageField(upload_to="post_photos/", null=True, blank=True)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title
