# Generated by Django 3.2.5 on 2021-07-08 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210708_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.CharField(blank=True, max_length=300, verbose_name='Description'),
        ),
    ]