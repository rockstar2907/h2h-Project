# Generated by Django 3.0.5 on 2020-07-22 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20200722_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='qauntity',
        ),
        migrations.AddField(
            model_name='cart',
            name='qty',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]