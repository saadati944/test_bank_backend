from django.db import models
from django.contrib.auth.models import User


class question(models.Model):
    Question=models.CharField(max_length=4096, null=False)

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name