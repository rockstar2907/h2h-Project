# Generated by Django 3.0.5 on 2020-07-22 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200722_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='item_name',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userorders',
            name='item_name',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
