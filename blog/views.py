from django.shortcuts import render
from django.db.models import Q
from .models import Post

# Create your views here.

def home_page(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(title__icontains=q) | Q(description__icontains=q))
        posts = Post.objects.filter(multiple_q)
    else:
        posts = Post.objects.all()
    context = {'posts':posts}            
    return render(request ,'blog/home_page.html' , context)
