# Generated by Django 3.2.13 on 2023-04-24 14:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20230424_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='art_published',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 24, 15, 24, 56, 83487), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_published',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 24, 15, 24, 56, 82987), verbose_name='date published'),
        ),
    ]