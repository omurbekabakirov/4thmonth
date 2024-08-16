from django.http import HttpResponse
from django.shortcuts import render
from post.models import Post


def hello_view(request):
    return HttpResponse("Hello_World")
def main_view(request):
    return render(request, 'main.html')


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})


def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})
