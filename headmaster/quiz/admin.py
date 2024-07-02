from django.contrib import admin
from .models import Quiz, Question, Answer, UserQuiz

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionInline(admin.TabularInline):
    model = Question

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'text')
    inlines = [AnswerInline]

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'is_correct')

class UserQuizAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'completed', 'score')

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(UserQuiz, UserQuizAdmin)
