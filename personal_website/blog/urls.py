from django.urls import path
from . import views
urlpatterns = [
    path("", views.f_1, name="home"),
    path("posts/", views.f_2)
]
