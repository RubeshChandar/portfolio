# Generated by Django 5.0 on 2025-01-04 19:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("still", "0003_alter_email_comments"),
    ]

    operations = [
        migrations.AlterField(
            model_name="email",
            name="role",
            field=models.CharField(max_length=100),
        ),
    ]