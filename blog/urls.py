from django.urls import path
from .views import *


urlpatterns = [
    path('',home_page , name='home_Page'),
    path('post/<int:pk>/',detail_post , name='detail_post'),
    path('post/<int:post_id>/comment/', add_comment, name='add_comment'),
]