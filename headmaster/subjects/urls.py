from django.urls import path
from . import views

urlpatterns = [
    # Subject URLs
    path('subjects/', views.subject_list, name='subject_list'),
    path('subject/<int:pk>/', views.subject_detail, name='subject_detail'),
    path('subject/new/', views.subject_create, name='subject_create'),
    path('subject/<int:pk>/edit/', views.subject_update, name='subject_update'),
    path('subject/<int:pk>/delete/', views.subject_delete, name='subject_delete'),

    # Lesson URLs
    path('subject/<int:subject_id>/lesson/new/', views.lesson_create, name='lesson_create'),
    path('subject/<int:subject_id>/lesson/<int:lesson_id>/edit/', views.lesson_update, name='lesson_update'),
    path('subject/<int:subject_id>/lesson/<int:lesson_id>/delete/', views.lesson_delete, name='lesson_delete'),
    path('lessons/', views.lesson_list, name='lesson_list'),
]
