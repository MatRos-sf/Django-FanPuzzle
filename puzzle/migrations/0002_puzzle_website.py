# Generated by Django 4.0.4 on 2022-05-16 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzle',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
