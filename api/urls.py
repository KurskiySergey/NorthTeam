from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.show_candidates, name="candidates"),
]