# Generated by Django 4.0.4 on 2022-06-03 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_profilephoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='photos',
        ),
    ]
