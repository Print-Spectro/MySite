# Generated by Django 3.2.13 on 2023-04-23 22:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_video_video_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_published',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 23, 23, 59, 1, 467031), verbose_name='date published'),
        ),
    ]
