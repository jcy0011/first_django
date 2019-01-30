import os
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from .models import Post
from .Forms import PostForm
# Create your views here.
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post.objects.create(**form.cleaned_data)
            return redirect('/dojo/')
        else:
            form = PostForm()
            return render(request, 'dojo/post_form.html', {
                'form' : form
            })

def mysum(request, numbers):
    # request: HttpRequest
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)

def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name,age))

def post_list1(request):
    name = 'j'
    return HttpResponse('''
    <h1>AskDjango</h1>
    <p>{name}</p>
    <p>여러분의 파이선 장고 페이스메이커가 되겠습니다.</p>
    '''.format(name=name))

def post_list2(request):
    name = 'jay'
    return render(request, 'dojo/post_list.html', {'name': name})

def post_list3(request):
    return JsonResponse({
        'message': '안녕 파이썬&장고',
        'items' : ['파이썬', '장고', 'Celery', 'Azure', 'AWS']
    }, json_dumps_params={'ensure_ascii': False})

def excel_download(request):
    filepath = os.path.join(settings.BASE_DIR, 'test_import.xlsx')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type = 'application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response