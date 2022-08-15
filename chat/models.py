from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Chat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now=True) 
