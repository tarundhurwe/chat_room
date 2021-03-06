from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length = 1000)

    def __str__(self) -> str:
        return str(self.name)

class Message(models.Model):
    value = models.CharField(max_length = 100000)
    date = models.DateTimeField(default = timezone.now, blank = True)
    user = models.CharField(max_length = 10000)
    room = models.CharField(max_length = 10000)

    def __str__(self):
        return str(self.user)