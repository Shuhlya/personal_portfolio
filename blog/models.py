from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    url = models.URLField()
    date = models.DateTimeField(auto_now_add=True)