from django.shortcuts import render , get_object_or_404 ,redirect
from django.http import JsonResponse
from django.db.models import Q
from .models import Post
from .forms import CommentForm , PostForm
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
            return JsonResponse({'success': True})  
    return JsonResponse({'success': False, 'errors': form.errors})


# create post
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  
            post.save()
            return redirect('home_Page')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})


# apdate post 

def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detail_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/update_post.html', {'form': form, 'post': post})


# delete post 
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home_Page')
    return render(request, 'blog/delete_post.html', {'post': post})