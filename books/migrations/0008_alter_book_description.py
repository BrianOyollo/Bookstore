# Generated by Django 3.2.5 on 2021-07-08 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, max_length=650, verbose_name='Description'),
        ),
    ]