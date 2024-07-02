from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.staff_profile_view, name='staff_profile'),
    path('list/', views.staff_list_view, name='staff_list'),
    path('dashboard/', views.staff_dashboard_view, name='staff_dashboard'),
]
