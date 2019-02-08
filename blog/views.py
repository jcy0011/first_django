from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Post
from .Forms import PostForm

# Create your views here.
def post_list(request):
    qs= Post.objects.all()
    q = request.GET.get('q','')
    if q:
        qs = qs.filter(title__icontains=q)
    # messages.error(request, 'error message test')
    return render(request, 'blog/post_list.html', {
        'post_list': qs,
        'q':q,
    })

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html',{
        'post': post,
    })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'saved the new post')
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form':form,
    })

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'edited the post')
            return redirect(post)
        pass
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {
        'form':form,
    })