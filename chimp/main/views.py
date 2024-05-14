from django.shortcuts import render 
from django.http import HttpResponse

def show_archive(request):
    return render(request, "main/archive.html")

def show_teacher(request):
    return render(request, "main/teacher.html")
    

