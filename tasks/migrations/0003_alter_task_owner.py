# Generated by Django 5.0.6 on 2024-07-14 07:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0002_alter_task_owner"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
