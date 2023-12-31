# Generated by Django 4.2.7 on 2023-12-11 00:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0003_contact_created_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="Email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="contact",
            name="Name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
