from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TestUser, Candidate

# Create your views here.
def main(request):
    return render(request, "main/index.html")

def test(request):
    return HttpResponse("Test")

def about(request):
    return render(request, "main/about.html")

def contacts(request):
    return render(request, "main/contacts.html")

def submit(request):
    # print(request.POST)
    post = request.POST
    name_info = post.get("name").split(" ")
    user = Candidate()
    user.first_name = name_info[0]
    user.second_name = name_info[1]
    user.third_name = name_info[2]
    user.phone = post.get("number")
    user.email = post.get("email")
    user.save()
    return render(request, "main/index.html")