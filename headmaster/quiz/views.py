from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, Answer, UserQuiz
from django.contrib.auth.decorators import login_required

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz.html', {'quizzes': quizzes})

def quiz_detail(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    questions = quiz.questions.all()
    return render(request, 'quiz/take_quiz.html', {'quiz': quiz, 'questions': questions})

@login_required
def submit_quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    questions = quiz.questions.all()
    user_quiz, created = UserQuiz.objects.get_or_create(user=request.user, quiz=quiz)
    
    if request.method == 'POST':
        score = 0
        total_questions = questions.count()
        
        for question in questions:
            correct_answer = question.answers.filter(is_correct=True).first()
            selected_answer_id = request.POST.get(str(question.id))
            selected_answer = question.answers.get(id=selected_answer_id) if selected_answer_id else None

            if selected_answer and selected_answer.is_correct:
                score += 1

        user_quiz.completed = True
        user_quiz.score = (score / total_questions) * 100
        user_quiz.save()
        
        return redirect('quiz_result', pk=user_quiz.pk)
    
    return render(request, 'quiz/take_quiz.html', {'quiz': quiz, 'questions': questions})

def quiz_result(request, pk):
    user_quiz = get_object_or_404(UserQuiz, pk=pk)
    return render(request, 'quiz/quiz_complete.html', {'user_quiz': user_quiz})
