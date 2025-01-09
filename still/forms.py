from django import forms
from .models import Message

placeholders = {
    "email_id": "Please enter your email *",
    "name": "Type in your full name *",
    "comments": "Write your message...",
    "company": "Enter the name of your company *",
}


class MessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.is_required = False
            self.fields[field].widget.attrs['placeholder'] = placeholders[field]

        self.fields["comments"].widget.attrs['rows'] = 4

    class Meta:
        fields = "__all__"
        model = Message
        labels = {
            "email_id": "Email",
            "name": "Full name",
        }
