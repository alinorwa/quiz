from django.shortcuts import render , get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from .models import Post
from .forms import CommentForm
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

def detail_post(request ,pk):
    post = get_object_or_404(Post , pk=pk)
    return render(request , 'blog/detail.html',{'post':post})


def add_comment(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post = Post.objects.get(pk=post_id)
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return JsonResponse({'success': True})  # Send JSON response indicating success
    return JsonResponse({'success': False, 'errors': form.errors})