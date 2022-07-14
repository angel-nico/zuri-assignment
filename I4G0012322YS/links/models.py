from logging.config import IDENTIFIER
from os import link
from django.db import models

# Create your models here.


from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse


class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(blank=True, unique=True, max_length=20)
    author = get_user_model
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


