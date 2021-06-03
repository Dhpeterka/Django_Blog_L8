from django.db import models
from django.contrib.auth.models import User # this is standard issue db in Django


class Post(models.Model):
    title = models.CharField(max_length=128) # char if max length is known, text if not.
    body = models.TextField(blank=True) # okay to be empty
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True) # stamps time at first save
    modified = models.DateTimeField(auto_now=True) # updates field to now every save
    published = models.DateTimeField(blank=True, null=True) # can be blank if not published