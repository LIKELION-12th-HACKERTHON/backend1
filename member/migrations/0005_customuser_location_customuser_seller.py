# Generated by Django 5.0.7 on 2024-07-22 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_remove_customuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='location',
            field=models.CharField(choices=[('강남구', '강남구'), ('강동구', '강동구'), ('강북구', '강북구'), ('강서구', '강서구'), ('관악구', '관악구'), ('광진구', '광진구'), ('구로구', '구로구'), ('금천구', '금천구'), ('노원구', '노원구'), ('도봉구', '도봉구'), ('동대문구', '동대문구'), ('동작구', '동작구'), ('마포구', '마포구'), ('서대문구', '서대문구'), ('서초구', '서초구'), ('성동구', '성동구'), ('성북구', '성북구'), ('송파구', '송파구'), ('양천구', '양천구'), ('영등포구', '영등포구'), ('용산구', '용산구'), ('은평구', '은평구'), ('종로구', '종로구'), ('중구', '중구'), ('중랄구', '중랄구')], default='', max_length=200),
        ),
        migrations.AddField(
            model_name='customuser',
            name='seller',
            field=models.CharField(choices=[('판매자', '판매자'), ('구매자', '구매자')], default='', max_length=200),
        ),
    ]