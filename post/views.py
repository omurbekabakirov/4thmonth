from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from post.forms import PostForm, SearchForm
from post.models import Post


def main_view(request):
    return render(request, 'main.html')


@login_required(login_url='post_lst')
def post_list_view(request):
    posts = Post.objects.all()
    search = request.GET.get('search', None)
    tag = request.GET.getlist('tags', None)
    search_form = SearchForm(request.GET)
    orderings = request.GET.getlist('orderings', None)

    if search:
        posts = posts.filter(Q(title__icontains=search) | Q(content__icontains=search))
    if tag:
        posts = posts.filter(tag__id__in=tag)
    page = int(request.GET.get('page', 1))
    limit = 5
    max_pages = posts.count() / limit
    if round(max_pages) < max_pages:
        max_pages = round(max_pages) + 1
    else:
        max_pages = round(max_pages)
    start = (page - 1) * limit
    end = page * limit
    posts = posts[start:end]
    if orderings:
        posts = posts.order_by(orderings)
    context = {'posts': posts, 'search_form': search_form, 'max_pages': range(1, max_pages + 1)}

    return render(request, 'posts/post_list.html', context=context)


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
