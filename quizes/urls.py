from django.urls import path
from .views import *



urlpatterns = [
    path('quiz/' , QuizListView.as_view() , name='main-view'),
    path('quiz/<int:pk>/' , quiz_view , name='quiz-view'),
    path('quiz/<int:pk>/save/' , save_data_view , name='save-view'),
    path('quiz/<int:pk>/data/' , quiz_data_view , name='quiz-data-quiz'),
]