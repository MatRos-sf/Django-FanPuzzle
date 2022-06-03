# Generated by Django 4.0.4 on 2022-06-03 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.TextField(default=None, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]