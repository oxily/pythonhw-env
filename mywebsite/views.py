from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import tb_news

# Create your views here.
def index(request):
    # return HttpResponse("Hello Django")
    data = {
        'fname' : "Orrathai",
        'lname' : "Oongsakun",
    }
    return render(request, 'mywebsite/index.html', data)
def hello(request, fname):
    return HttpResponse("My name is" + fname)

def addNews(request):
    return render(request, 'mywebsite/addNews.html')

def recordNews(request):
    topic = request.POST['topic_news']
    detail = request.POST['detail_news']
    photo = request.FILES['photo_news']
    content = tb_news(topic_news=topic, detail_news=detail, photo_news=photo)
    content.save()
    return redirect('/contentNews')

def contentNews(request):
    content = tb_news.objects.all()
    data={
        'content' : content
    }
    return render(request, 'mywebsite/contentNews.html', data)

def contentEdit(request):
    id = request.GET['id']
    result = tb_news.objects.filter(pk=id)
    data = {
        'result' : result
    }
    return render(request, 'mywebsite/contentEdit.html', data)

# def resultPage(request):
#     topic = request.POST['topic_news']
#     detail = request.POST['detail_news']
#     data ={
#         'topic' : topic,
#         'detail' : detail,
#     }

#     return render(request, 'mywebsite/resultPage.html', data)