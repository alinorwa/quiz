from django.urls import path
from .views import generatepassword


urlpatterns = [
    path('password/',generatepassword , name='password')
]
