from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path("test/", views.test, name="test"),
    path("about/", views.about, name="about"),
    path("contacts/", views.contacts, name='contacts'),
    path("submit/", views.submit, name="submit"),
]