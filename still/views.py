from django.shortcuts import render, redirect
from .forms import EmailForm
from django.views import View
from django.contrib import messages
from .constants import experiences


def index(request):
    return render(request, "still/index.html")


class ResumeView(View):
    def get(self, request):
        emailform = EmailForm()
        return render(request, "still/resume.html", {
            "form": emailform,
        })

    def post(self, request):
        emailform = EmailForm(request.POST)

        if emailform.is_valid():
            emailform.save()
            messages.success(
                request, "You request was completed successfully !")
            return redirect("resume")

        messages.error(request, "You're message wasn't sent")
        return render(request, "still/resume.html", {
            "form": emailform,
        })


# def sendEmail(request):
#     add = ['rubeshchander.rc@gmail.com']
#     if request.method == "POST":
#         add.append(request.POST["email_id"])
#         name = request.POST["name"]
#         message = request.POST["comments"]
#         send_mail(
#             subject=f"Thank you {name} for viewing my website",
#             message="Send from django project",
#             recipient_list=add[1:],
#             from_email=None,
#             fail_silently=False,
#         )

#     return redirect("resume")


def experience(request):
    return render(request, "still/experience.html", {
        "experiences": experiences
    })
