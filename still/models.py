from django.db import models


class Message(models.Model):
    email_id = models.EmailField()
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    comments = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} enquired for {self.company}"


class Experience(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    year = models.CharField(max_length=100)
    company = models.TextField()
    education = models.BooleanField(default=False)
    heading = models.CharField(max_length=255)
    content = models.JSONField()  # Bullet points
    skills = models.JSONField()   # Skills list

    def __str__(self):
        return self.heading

    class Meta:
        ordering = ["created_at"]
