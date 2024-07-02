# staff/forms.py

from django import forms
from .models import StaffProfile

class StaffProfileForm(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = ['position', 'hire_date']
