from django.db import models

from inheritance.models import ParentModel, ChildManager


class Post(ParentModel):
    title = models.CharField(max_length=50)

    objects = models.Manager()
    children = ChildManager()

    def __unicode__(self):
        return self.title

    def get_parent_model(self):
        return Post


class Article(Post):
    text = models.TextField()


class Photo(Post):
    image = models.ImageField(upload_to='photos/')


class Link(Post):
    url = models.URLField()
