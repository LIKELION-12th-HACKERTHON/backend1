# Generated by Django 5.0.7 on 2024-07-23 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boss', '0006_remove_post_user_post_boss'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='boss',
            new_name='user',
        ),
    ]
