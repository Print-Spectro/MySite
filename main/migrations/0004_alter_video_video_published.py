# Generated by Django 4.2 on 2023-04-23 18:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_rename_tutorial_published_video_video_published"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="video_published",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 23, 19, 48, 1, 862118),
                verbose_name="date published",
            ),
        ),
    ]