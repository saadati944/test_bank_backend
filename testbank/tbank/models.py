from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Question(models.Model):
    is_test = models.BooleanField(null=True, default=False)
    title = models.CharField(max_length=250, null=True)
    description = models.CharField(max_length=4096, null=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=4096, null=True)


class TestChoice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice = models.CharField(max_length=100, null=True)
    is_answer = models.BooleanField(null=True,default=False)


class Quiz(models.Model):
    name = models.CharField(max_length=250, null=True)
    description = models.CharField(max_length=4096, null=True)
    question = models.ManyToManyField(Question)