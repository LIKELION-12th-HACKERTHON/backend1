# Generated by Django 5.0.7 on 2024-07-25 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_remove_customuser_location_customuser_city_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='detaillocation',
            new_name='detail_location',
        ),
    ]
