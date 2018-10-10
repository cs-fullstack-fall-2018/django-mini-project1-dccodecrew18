from django.db import models
from django.db import models
import datetime
from django.utils import timezone

class Post(models.Model):
    TeacherName = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date punched in ')
    def __str__(self):
        return self.Post_text

    def was_published_recently(self):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
# Create your models here.This is where templates will be formes as a basis for
# the forms , the time punch sheets the teachers fill out . Name , date time punched in etc
#  Kenn said migrate model changes each time you make them
