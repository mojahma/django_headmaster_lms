from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import register, home, CustomLoginView, student_profile, teacher_profile, admin_profile, profile

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'), 
    path('profile/student/', student_profile, name='student_profile'),
    path('profile/teacher/', teacher_profile, name='teacher_profile'),
    path('profile/admin/', admin_profile, name='admin_profile'),
    path('profile/', profile, name='profile'),
]
