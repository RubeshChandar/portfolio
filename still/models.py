from django.db import models


class Email(models.Model):
    email_id = models.EmailField(primary_key=True)
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    comments = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} enquired for {self.company}"
