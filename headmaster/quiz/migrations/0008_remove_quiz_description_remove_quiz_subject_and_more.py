# Generated by Django 5.0.6 on 2024-07-01 20:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_alter_quiz_subject_delete_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='description',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='userquiz',
            name='completed',
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='userquiz',
            name='score',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='quiz.question')),
            ],
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
