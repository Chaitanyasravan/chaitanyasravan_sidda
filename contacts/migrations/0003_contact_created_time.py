# Generated by Django 4.2.7 on 2023-12-08 22:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0002_auto_20231208_2239"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="created_time",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]