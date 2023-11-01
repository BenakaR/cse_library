# Generated by Django 4.2.6 on 2023-10-28 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("isbn", models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.TextField(max_length=20)),
                ("fine", models.IntegerField(max_length=4)),
                (
                    "issued",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="website.book"
                    ),
                ),
            ],
        ),
    ]
