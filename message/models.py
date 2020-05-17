from django.db import models
import datetime


# Create your models here.

class Message(models.Model):
    username = models.CharField(max_length=16)
    message = models.TextField()
    addtime = models.DateTimeField(auto_now_add=datetime.datetime)

    def __str__(self):
        return self.username