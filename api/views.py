from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from main.models import Candidate
import os
from config import STATIC_DIR
# Create your views here.

@login_required(login_url="/api/login")
def show_candidates(request, page=None):
    candidates = Candidate.all()
    pagination_list_value = 3
    max_pages = (len(candidates)-1) // pagination_list_value + 1
    if page is None:
        page = 1
    if page > max_pages > 0:
        page = max_pages
    list_candidates = candidates[(int(page)-1)*pagination_list_value: (int(page)-1)*pagination_list_value + pagination_list_value]
    context = {
        'candidates': list_candidates,
        'page': int(page),
        'max_page': max_pages,
        'page_list': range(1, max_pages+1)
    }
    return render(request, "api/api_candidates.html", context=context)


@login_required(login_url="/api/login")
def delete_user(request, user_id=None, page=None):
    if user_id is not None and isinstance(user_id, int):
        user = Candidate.objects.filter(id=user_id)
        if user is not None:
            user.delete()
    if page is None:
        page = 1
    return redirect(show_candidates, page=page)


@login_required(login_url="/api/login")
def get_profile_photo(request, user_id):
    user = Candidate.objects.filter(id=user_id)
    if user is not None:
        bf_photo = user[0].photo
        return HttpResponse(content=bf_photo, status=200)
    return HttpResponse(status=500)


def login(request):
    if request.user.is_authenticated:
        return redirect(show_candidates)
    elif request.method == "POST":
        post = request.POST
        username = post.get("name")
        password = post.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect(show_candidates)
    return render(request, "api/login.html")


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("/")