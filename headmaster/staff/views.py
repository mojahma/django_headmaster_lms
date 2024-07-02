# staff/views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import StaffProfile
from .forms import StaffProfileForm

@login_required
def staff_profile_view(request):
    profile = get_object_or_404(StaffProfile, user=request.user)
    if request.method == 'POST':
        form = StaffProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = StaffProfileForm(instance=profile)
    return render(request, 'staff/staff_profile.html', {'form': form})

def staff_list_view(request):
    staff_members = StaffProfile.objects.all()
    return render(request, 'staff/staff_list.html', {'staff_members': staff_members})

@login_required
def staff_dashboard_view(request):
    return render(request, 'staff/staff_dashboard.html')

