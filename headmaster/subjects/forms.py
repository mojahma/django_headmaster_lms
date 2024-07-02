from django import forms
from .models import Subject, Lesson

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'image', 'description']

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['subject', 'image', 'description', 'content', 'external_link']
