from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.views.generic import  ListView

class QuizListView(ListView):
    model = Quiz
    template_name = "quizes/main.html"


def quiz_view(request,pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request,'quizes/quiz.html',{'obj':quiz})   


def quiz_data_view(request,pk):
    quiz = Quiz.objects.get(pk=pk)
    question = []
    for q in quiz.get_questions():
        answer = []
        for a in q.get_answer():
            answer.append(a.text)
        question.append({str(q): answer})
    return  JsonResponse({'data':question , 'time':quiz.time })       


def save_data_view(request,pk):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        questions = []
        if request.method == 'POST':
            data = request.POST
            data_ = dict(data.lists())
            data_.pop('csrfmiddlewaretoken')

            for k in data_.keys():
                question = Question.objects.get(text=k)
                questions.append(question)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)
            if a_selected != '':
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else: 
                        if a.correct:
                            correct_answer = a.text
                results.append({str(q):{'correct_answer':correct_answer ,'answred':a_selected }})            

            else:
                results.append({str(q): 'not answerd'})

        score_ = score * multiplier
        Result.objects.create(quiz=quiz , user=user , score = score_)  

        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'passed': True , 'score':score_ , 'results': results}) 
        else: 
           return JsonResponse({'passed':False , 'score':score_ , 'results': results})