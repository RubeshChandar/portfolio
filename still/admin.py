from django.contrib import admin
from .models import Message
# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ("name", "company")
    readonly_fields = ("created_at",)


admin.site.register(Message, MessageAdmin)
