# Generated by Django 4.2.6 on 2023-11-02 06:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="issue",
        ),
    ]
