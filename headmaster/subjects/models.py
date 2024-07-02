from django.db import models
from quiz.models import Quiz

class Subject(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='subject_images/')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    subject = models.ForeignKey(Subject, related_name='lessons', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='lesson_images/')
    description = models.CharField(max_length=255)
    content = models.TextField()
    external_link = models.URLField(blank=True)
    


    def __str__(self):
        return self.description
