from django.shortcuts import render, redirect, HttpResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User


def home(request): 

    context = {
        'posts' : Post.objects.all()        
    }
    return render(request, "blog_app/home.html", context)

def about(request):
    return render(request, "blog_app/about.html", {'title' : 'About'})

def mentor_page(request):
    return render(request, "blog_app/mentorinfo.html")

def post_detail(request, post_id):
    context = {
        "post": Post.objects.get(id=post_id)
    }
    return render(request, 'blog_app/post_detail.html', context)

def add_comment_to_post(request, post_id):
    post1 = Post.objects.get(id=post_id)
    author1 = User.objects.get(id=request.user.id)
    Comment.objects.create(
        post = post1,
        author = author1,
        text = request.POST["text"]
    )
    return redirect(f'/post/{post_id}')


def new_post(request):
    if request.method == 'POST':
        author1 = User.objects.get(id=request.user.id)
        Post.objects.create(
            author = author1,
            content = request.POST["content"])
        return redirect('/')
    else:
        return render(request, 'blog_app/new.html')
    
    
def destroy(request, post_id):
    d = Post.objects.get(id=post_id)
    d.delete()
    return redirect('/')

def comment_remove(request, comment_id, post_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect(f'/post/{post_id}')

