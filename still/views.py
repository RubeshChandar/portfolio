import os
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render, redirect
from .forms import MessageForm
from django.views import View
from django.contrib import messages
from .constants import experiences
from django.core.mail import send_mail


def index(request):
    return render(request, "still/index.html")


class ResumeView(View):
    def get(self, request):
        messageForm = MessageForm()
        return render(request, "still/resume.html", {
            "form": messageForm,
        })

    def post(self, request):
        messageForm = MessageForm(request.POST)

        if messageForm.is_valid():
            messageForm.save()
            messages.success(
                request, "You request was completed successfully !")
            sendEmail(messageForm.cleaned_data)
            return redirect("resume")

        messages.error(request, "You're message wasn't sent")
        return render(request, "still/resume.html", {
            "form": messageForm,
        })


def pdf_view(request):
    path = os.path.join(settings.MEDIA_ROOT, "cv.pdf")
    response = FileResponse(open(path, 'rb'), content_type="application/pdf")
    response["Content-Disposition"] = "filename={}"
    return response


def sendEmail(data):
    name = data["name"]
    message = data["comments"]
    mail_id = data['email_id']
    company = data['company']
    send_mail(
        subject=f"You got one new message from {name}",
        message=f"{name} sent you a new message <br> Message: {message} <br>You can reply to {mail_id}",
        recipient_list=['rubeshchander.rc@gmail.com'],
        from_email=None,
        fail_silently=False,
        html_message=f"{name} from {company} sent you a new message <br> Message: {message} <br>You can reply to {mail_id}",
    )

    return redirect("resume")


def experience(request):
    return render(request, "still/experience.html", {
        "experiences": experiences
    })
