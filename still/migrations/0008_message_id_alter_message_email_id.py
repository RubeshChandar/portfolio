# Generated by Django 5.0 on 2025-01-09 01:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("still", "0007_rename_email_message"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=1,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="message",
            name="email_id",
            field=models.EmailField(max_length=254),
        ),
    ]
