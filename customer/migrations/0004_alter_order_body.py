# Generated by Django 5.0.7 on 2024-07-23 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_order_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='body',
            field=models.TextField(default=''),
        ),
    ]