# Generated by Django 4.0.4 on 2022-06-01 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzle', '0004_alter_puzzle_options_alter_puzzle_likes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_add', models.IntegerField(default=0)),
                ('for_daily_login', models.IntegerField(default=1)),
                ('for_comments', models.IntegerField(default=0)),
                ('for_edit', models.IntegerField(default=0)),
                ('for_like', models.IntegerField(default=0)),
                ('for_visit', models.IntegerField(default=0)),
                ('for_bonus', models.IntegerField(default=0)),
            ],
        ),
    ]
