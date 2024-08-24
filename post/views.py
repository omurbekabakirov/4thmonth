from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from post.forms import PostForm
from post.models import Post


def hello_view(request):
    return HttpResponse("Hello_World")


def main_view(request):
    return render(request, 'main.html')


@login_required(login_url='post_lst')
def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})


@login_required(login_url='post_detail')
def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})


@login_required(login_url='post_create')
def post_create_view(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'posts/post_create.html', context={'form': form})
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'posts/create.html', context={'form': form})
        image = form.cleaned_data.get('image')
        title = form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')
        rating = form.cleaned_data.get('rating')
        Post.objects.create(
            title=title,
            content=content,
            rating=rating,
            image=image)
        return redirect('/post_lst/')



