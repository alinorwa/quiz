from django.urls import path
from .views import *



urlpatterns = [
    path('' , QuizListView.as_view() , name='main-view'),
    path('<int:pk>/' , quiz_view , name='quiz-view'),
    path('<int:pk>/save/' , save_data_view , name='save-view'),
    path('<int:pk>/data/' , quiz_data_view , name='quiz-data-quiz'),
]