from django.db import models

# Create your models here.
from django.db import models

# Example model


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_created=True)
