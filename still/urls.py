from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("resume", views.resume, name="resume"),
    path("contact-me", views.contact, name="contact"),
]
