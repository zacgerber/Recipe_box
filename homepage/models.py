from django.db import models
from django.utils import timezone
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=80)
    Bio = models.TextField(default='none')

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    instructions = models.TextField(default="none")
    time_required = models.CharField(max_length=50, default="none")
    post_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.author.name} "
