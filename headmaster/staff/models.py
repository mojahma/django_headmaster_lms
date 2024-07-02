from django.db import models
from django.conf import settings

class StaffProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
    image = models.ImageField(upload_to='staff/images/', null=True, blank=True)  
    def __str__(self):
        return self.user.username
    class Meta:
        ordering = ['position']