from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000000)
    datetime = models.DateTimeField(default=datetime.now, blank=True)
    user = models.TextField(max_length=100000)
    # user_id = models.TextField(max_length=100)
