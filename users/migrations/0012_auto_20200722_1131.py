# Generated by Django 3.0.5 on 2020-07-22 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_cart_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='rest_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userorders',
            name='rest_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
