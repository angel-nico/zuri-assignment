from logging.config import IDENTIFIER
from os import link
from django.db import models

# Create your models here.

class linksmodel(link):
    target_url = models.URLField(max_length=200)
