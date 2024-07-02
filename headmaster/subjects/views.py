from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Subject, Lesson
from .forms import SubjectForm, LessonForm
from quiz.models import UserQuiz 

# Helper function to check if user is admin
def user_is_admin(user):
    return user.is_authenticated and user.is_staff

# Views for Subjects
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects/subject_list.html', {'subjects': subjects})


##### Subject Detail
@login_required
def subject_detail(request, pk):
    # Check if user is authenticated
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to the login page if not logged in

    subject = get_object_or_404(Subject, pk=pk)
    lessons = subject.lessons.all()

    for lesson in lessons:
        try:
            lesson.quiz_completed = UserQuiz.objects.filter(user=request.user, quiz=lesson.quiz, completed=True).exists()
        except AttributeError:
            lesson.quiz_completed = False

    context = {'subject': subject, 'lessons': lessons}
    return render(request, 'subjects/subject_detail.html', context)
######


@login_required
@user_passes_test(user_is_admin)
def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'subjects/subject_form.html', {'form': form})

@login_required
@user_passes_test(user_is_admin)
def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        form = SubjectForm(request.POST, request.FILES, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'subjects/subject_form.html', {'form': form})

@login_required
@user_passes_test(user_is_admin)
def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('subject_list')
    return render(request, 'subjects/subject_confirm_delete.html', {'subject': subject})

# Views for Lessons
@login_required
@user_passes_test(user_is_admin)
def lesson_create(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.subject = subject
            lesson.save()
            return redirect('subject_detail', pk=subject_id)
    else:
        form = LessonForm()
    return render(request, 'subjects/lesson_form.html', {'form': form, 'subject': subject})

@login_required
@user_passes_test(user_is_admin)
def lesson_update(request, subject_id, lesson_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('subject_detail', pk=subject_id)
    else:
        form = LessonForm(instance=lesson)
    return render(request, 'subjects/lesson_form.html', {'form': form, 'subject': subject})

@login_required
@user_passes_test(user_is_admin)
def lesson_delete(request, subject_id, lesson_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == 'POST':
        lesson.delete()
        return redirect('subject_detail', pk=subject_id)
    return render(request, 'subjects/lesson_confirm_delete.html', {'lesson': lesson, 'subject': subject})

# Lesson views
@login_required
@user_passes_test(user_is_admin)
def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'subjects/lesson_list.html', {'lessons': lessons})
