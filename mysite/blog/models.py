from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_gueryset()\
                        .filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    # This class need for define to status of posts
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)  # Title of post
    slug = models.SlugField(max_length=250)  # This point for URLs
    # Define to relationship many-to-single, every post been writen specific User
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,  # Define behavior when User was deleted, also deleting his
                               # all posts
                               related_name='blog_posts'
                               )
    body = models.TextField()  # body of post

    # This code needs for define date and time, it's show status of post(created, updated, publish)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Limit to value of field variants from Status.choices - draft and published, and set to default status - draft
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    # This class define Meta-data of model. Show variant presentation of posts,  '-' means chronological order
    class Meta:
        ordering = ['-publish']
        # This options means the index of database, needs for future migrations of database
        indexes = [
            models.Index(fields=['-publish'])
        ]

    # This method need for presentation name of objects
    def __str__(self):
        return self.title
