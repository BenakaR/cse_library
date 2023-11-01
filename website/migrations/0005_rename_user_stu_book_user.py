# Generated by Django 4.2.6 on 2023-10-29 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("website", "0004_alter_user_issued"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="User",
            new_name="Stu",
        ),
        migrations.AddField(
            model_name="book",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
