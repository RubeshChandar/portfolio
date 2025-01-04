from django import forms
from .models import Email


class EmailForm(forms.ModelForm):

    class Meta:
        fields = "__all__"
        model = Email
        labels = {
            "email_id": "Email",
            "name": "Full name",
        }
