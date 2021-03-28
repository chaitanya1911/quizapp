from django.shortcuts import render
from django.http import HttpResponse
from .models import Quiz,Question,Choice

def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'quiz_app/index.html',{'quiz':Quiz.objects.all()})

def details(request,quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions_list = quiz.questions.all()
    return render(request,'quiz_app/display.html',{'questions_list':questions_list,'quizId':quiz_id})

def results(request,quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.questions.all()
    results=0
    total=questions.count()
    for question in questions:
        x = request.POST[question.question_text]
        
        if  x == "True":
            print(request.POST[question.question_text])
            results+=1

    return render(request,'quiz_app/results.html',{'result':results,'total':total})   