# Generated by Django 3.2.5 on 2021-07-08 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210708_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='cover',
        ),
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]
