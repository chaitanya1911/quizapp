from django.contrib import admin
from django.urls import path
from . import views

app_name='student'

urlpatterns = [
    path('', views.home,name='home') ,
    path('details/<int:quiz_id>/', views.details,name='quiz-details'),
    path('results/<int:quiz_id>', views.results,name='quiz-results'),
    path('index/',views.index,name='index'),
]