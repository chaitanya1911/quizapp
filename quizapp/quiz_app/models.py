from django.db import models
from django.utils import timezone
import datetime
from django.urls import reverse


class Student(models.Model):
    student_name=models.CharField(max_length=100)

    def __str__(self):
        return self.student_name


class Quiz(models.Model):
    quiz_name = models.CharField(max_length=200)
    quiz_date= models.DateField('Date Published')
    quiz_time=models.TimeField('Time Published')

    def __str__(self):
        return self.quiz_name
        
    def get_absolute_url(self):
        return reverse('teacher:quizdetail',kwargs={'pk':self.pk})



class Question(models.Model):
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE,related_name='questions')
    question_text = models.CharField(max_length=400)

    def __str__(self):
        return self.question_text

    


class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE,related_name='choices')
    choice_text=models.CharField(max_length=200)
    ans = models.BooleanField(default = False)

    def __str__(self):
        return self.choice_text