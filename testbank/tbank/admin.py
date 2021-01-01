from django.contrib import admin
from .models import *

class UserProfileAdmin(admin.ModelAdmin):
    list_display=['__str__', 'get_friends', 'get_students', 'get_teachers']

class QuestionAdmin(admin.ModelAdmin):
    list_display=['title', 'isprivate', 'owner', 'mode', 'get_tags', 'question', 'get_answers']

class QuizAdin(admin.ModelAdmin):
    list_display=['name', 'owner.first_name', 'isprivate', 'description' ,'get_questions']

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Question, QuestionAdmin)