# Generated by Django 4.2.6 on 2023-11-02 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0004_book_issue_to"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="issue_to",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="website.student",
            ),
        ),
    ]
