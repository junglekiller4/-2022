# Generated by Django 4.1.2 on 2022-12-06 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printing3d', '0006_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='user3d',
            name='name',
            field=models.TextField(default=' ', max_length=255, verbose_name='Имя'),
        ),
    ]
