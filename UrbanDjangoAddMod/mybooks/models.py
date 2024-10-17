from django.db import models


class Book(models.Model):
    objects = None
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title
