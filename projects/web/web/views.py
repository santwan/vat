from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse("This is About Page")

def index1(request):
    data = {
        "title":"Django"
    }
    return render(request, 'index.html', data)