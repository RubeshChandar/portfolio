from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("resume", views.ResumeView.as_view(), name="resume"),
    # path("send-email", views.sendEmail),
]
