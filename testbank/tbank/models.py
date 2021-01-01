from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    students = models.ManyToManyField(User, related_name='students')
    teachers = models.ManyToManyField(User, related_name='teachers')
    friends = models.ManyToManyField(User, related_name='friends')
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Answer(models.Model):
    answer=models.CharField(max_length=2048, default='')


class Question(models.Model):
    owner=models.ForeignKey(User, on_delete=models.PROTECT, default='')

    DESCRIPTIVE = 'DE' #The answer is not fixed and someone should check it.
    MULTICHOICE = 'MC' #The user must select the answer from the available answers.
    CONSTANT = 'CO'    #The answer is a fixed value, like a word.
    questionMode = [
        (DESCRIPTIVE, 'DESCRIPTIVE'),
        (MULTICHOICE, 'MULTICHOICE'),
        (CONSTANT, 'CONSTANT'),
    ]
    mode = models.CharField(
        max_length=2,
        choices=questionMode,
        default=MULTICHOICE,
    )

    isprivate = models.BooleanField(default=False)
    #tags = models.ManyToManyField()
    title=models.CharField(max_length=120, null=False, blank=False, default='title')
    question = models.CharField(max_length=4096, null=True, blank=False)
    answers=models.ManyToManyField(Answer, related_name='answers')

    def __str__(self):
        return self.title


class Quiz(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False, default="quiz")
    owner=models.ForeignKey(User, on_delete=models.PROTECT, default='')
    # todo : add a field to describe who can access this quiz
    isprivate=models.BooleanField(default=False)
    description = models.CharField(max_length=4096, null=True)
    questions=models.ManyToManyField(Question, related_name='questions')