from django.db import models
from django.contrib.auth.models import User
import random
# Create your models here.
DIFF_CHOICES =  (
    ('easy','easy'),
    ('medium','medium'),
    ('hard','hard'),
)

class Quiz(models.Model):
    name                   = models.CharField(max_length=120)
    topic                  = models.CharField(max_length=120)
    number_of_questions    = models.IntegerField()
    time                   = models.IntegerField(help_text='duration of the quiz in minutes')
    required_score_to_pass = models.IntegerField(help_text='required score in %')
    difficluty             = models.CharField(max_length=6 , choices=DIFF_CHOICES)
    created                = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name} -- {self.topic}'
    
    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]
    
    class Meta:
        verbose_name_plural = 'Quizes'


# ============================ 
class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
    def get_answer(self):
        return self.answer_set.all()

class Answer(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'question : {self.question.text} , answer : {self.text} , correct : {self.correct}' 
    
    def get_answer(self):
        pass

# ============================ 
class Result(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)