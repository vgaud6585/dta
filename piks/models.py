from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
# Create your models here.
class User(models.Model):
   usr_age = models.IntegerField()
   usr_image = models.ImageField(upload_to='images/')
