# Generated by Django 4.2 on 2023-04-23 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_rename_tutorial_video"),
    ]

    operations = [
        migrations.RenameField(
            model_name="video",
            old_name="tutorial_published",
            new_name="video_published",
        ),
    ]
