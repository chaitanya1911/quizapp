
from django.urls import path
from . import views

app_name='teacher'

urlpatterns=[
    path('teacher/quiz/',views.QuizListView.as_view(),name='quizlist'),
    path('teacher/quiz/<int:pk>/',views.QuizDetailView.as_view(),name='quizdetail'),
    path('teacher/quiz/create/',views.QuizCreateView.as_view(),name='quizcreate'),
    path('teacher/quiz/update/<int:pk>/',views.QuizUpdateView.as_view(),name='quizupdate'),
    path('teacher/quiz/delete/<int:pk>/',views.QuizDeleteView.as_view(),name='quizdelete'),

     path('teacher/quiz/createquestion/<int:pk>/',views.QuestionCreateView.as_view(),name='questionadd'),
     path('teacher/quiz/update/<int:pk>/question/<int:p>/',views.QuestionUpdateView.as_view(),name='questionupdate'),
     
    path('teacher/quiz/create/<int:pk>/question/<int:p>/choice',views.ChoiceCreateView.as_view(),name='choiceadd'),
     path('teacher/quiz/create/<int:pk>/question/<int:p>/choice/<int:a>',views.ChoiceUpdateView.as_view(),name='choiceupdate'),
]