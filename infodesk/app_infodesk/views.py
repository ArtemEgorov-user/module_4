from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return HttpResponse("<h1> всёе ок </h2>")

def index(request):
    return render(request, "index.html")

    