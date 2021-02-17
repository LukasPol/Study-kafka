from django.conf import settings
from django.db import models
from django.utils import timezone


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title