from django.contrib import admin
from .models import Message, Experience
# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ("name", "company")
    readonly_fields = ("created_at",)


class ExperienceAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "modified")
    list_display = ("heading",)


admin.site.register(Message, MessageAdmin)
admin.site.register(Experience, ExperienceAdmin)
