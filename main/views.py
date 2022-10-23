from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TestUser, Candidate
from .utils import correct_name

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
    print(name_info)
    user = Candidate()
    user.first_name, user.second_name, user.third_name = correct_name(name_info)
    user.phone = post.get("phone")
    user.email = post.get("email")
    user.save()
    return render(request, "main/index.html")