from django.urls import path
from .views import *


urlpatterns = [
    path('',home_page , name='home_Page'),
    path('create_post/',create_post , name='create_post'),
    path('post/<int:pk>/',detail_post , name='detail_post'),
    path('post/<int:pk>/edit/', update_post, name='update_post'),
    path('post/<int:pk>/delete/', delete_post, name='delete_post'),
    path('post/<int:post_id>/comment/', add_comment, name='add_comment'),
]