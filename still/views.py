from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import EmailForm


def index(request):
    return render(request, "still/index.html")


def resume(request):
    emailform = EmailForm()
    return render(request, "still/resume.html", {
        "form": emailform,
    })


def sendEmail(request):
    add = ['rubeshchander.rc@gmail.com']
    if request.method == "POST":
        add.append(request.POST["email_id"])
        name = request.POST["name"]
        message = request.POST["comments"]
        send_mail(
            subject=f"Thank you {name} for viewing my website",
            message="Send from django project",
            recipient_list=add[1:],
            from_email=None,
            fail_silently=False,
        )

    return redirect("resume")
