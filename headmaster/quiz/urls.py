from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('<int:pk>/', views.quiz_detail, name='quiz_detail'),
    path('<int:pk>/submit/', views.submit_quiz, name='submit_quiz'),
    path('result/<int:pk>/', views.quiz_result, name='quiz_result'),
]
