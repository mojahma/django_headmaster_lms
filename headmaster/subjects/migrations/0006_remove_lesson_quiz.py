# Generated by Django 5.0.6 on 2024-07-01 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0005_alter_lesson_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='quiz',
        ),
    ]
