# Generated by Django 5.0.7 on 2024-07-23 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boss', '0007_rename_boss_post_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='boss',
        ),
    ]
