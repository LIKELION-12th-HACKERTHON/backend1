# Generated by Django 5.0.7 on 2024-07-25 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_order_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='location',
        ),
    ]
