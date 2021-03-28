from django.shortcuts import render
from django.views.generic import (View,TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
from quiz_app import models


class QuizListView(ListView):
    context_object_name='quizs'
    model=models.Quiz
    template_name='teacher/quiz_list.html'

class QuizDetailView(DetailView):
    context_object_name='quiz_detail'
    model=models.Quiz
    template_name='teacher/quiz_detail.html'


class QuizCreateView(CreateView):
    fields=('quiz_name','quiz_date','quiz_time')
    model=models.Quiz
    template_name='teacher/quiz_form.html'

class QuestionCreateView(CreateView):
    fields=('quiz','question_text')
    model=models.Question
    template_name='teacher/question_form.html'
    success_url=reverse_lazy('teacher:quizlist')

class ChoiceCreateView(CreateView):
    fields=('question','choice_text','ans')
    model=models.Choice
    template_name='teacher/question_form.html'
    success_url=reverse_lazy('teacher:quizlist')



class QuizUpdateView(UpdateView):
    fields=('quiz_name','quiz_date','quiz_time')
    model=models.Quiz
    template_name='teacher/quiz_form.html'

class QuestionUpdateView(UpdateView):
    fields=('quiz','question_text')
    model=models.Question
    template_name='teacher/question_form.html'
    success_url=reverse_lazy('teacher:quizlist')

class ChoiceUpdateView(UpdateView):
    fields=('choice_text','ans')
    model=models.Choice
    template_name='teacher/question_form.html'
    success_url=reverse_lazy('teacher:quizlist')

class QuizDeleteView(DeleteView):
    model=models.Quiz
    template_name='teacher/quiz_confirm_delete.html'
    success_url=reverse_lazy('teacher:quizlist')    

class QuestionDeleteView(DeleteView):
    template_name='teacher/question_confirm_delete.html'
    model=models.Question
    success_url=reverse_lazy('teacher:quizlist') 

