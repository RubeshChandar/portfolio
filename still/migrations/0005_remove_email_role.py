# Generated by Django 5.0 on 2025-01-04 20:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("still", "0004_alter_email_role"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="email",
            name="role",
        ),
    ]