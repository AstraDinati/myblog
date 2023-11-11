# blog/models.py
from django.db import models
from taggit.managers import TaggableManager


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @classmethod
    def get_all_tags(cls):
        return cls.objects.all()


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    photo = models.ImageField(upload_to="post_photos/", null=True, blank=True)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title

    def set_tags(self, tags):
        existing_tags = Tag.get_all_tags()
        tag_objects = []

        for tag in tags:
            tag_instance, created = existing_tags.get_or_create(name=tag)
            tag_objects.append(tag_instance)

        self.tags.set(tag_objects)
