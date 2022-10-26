from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.show_candidates, name="candidates"),
    path("users/<int:page>", views.show_candidates, name="page-candidates"),
    path("delete_user/<int:user_id>/<int:page>", views.delete_user, name="deluser"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]