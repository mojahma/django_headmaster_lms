from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import StudentRegistrationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'home.html')

class CustomLoginView(auth_views.LoginView):
    template_name = 'login.html'

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home or any other page
    else:
        form = StudentRegistrationForm()
    return render(request, 'register.html', {'form': form})


# User Dashboard
@login_required
def student_profile(request):
    if request.user.is_student:
        return render(request, 'student_profile.html')
    else:
        return redirect('home')

@login_required
def teacher_profile(request):
    if request.user.is_teacher:
        return render(request, 'teacher_profile.html')
    else:
        return redirect('home')

@login_required
def admin_profile(request):
    admin = request.user  # Assuming admin is the authenticated user
    context = {
        'admin': admin,
    }
    return render(request, 'admin_profile.html', context)

class CustomLoginView(auth_views.LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        user = self.request.user
        if user.is_superuser:
            return reverse('admin_profile')
        elif user.is_teacher:
            return reverse('teacher_profile')
        elif user.is_student:
            return reverse('student_profile')
        else:
            return reverse('home')
        
#  file that handles displaying the user's profile.
@login_required
def profile(request):
    if request.user.is_staff:
        return render(request, 'admin_profile.html')
    elif request.user.groups.filter(name='teachers').exists():
        return render(request, 'teacher_profile.html')
    else:
        return render(request, 'student_profile.html')