# Generated by Django 4.0.4 on 2022-05-31 20:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('fullname', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=60, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='company/')),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number_of_pieces', models.IntegerField()),
                ('ean_code', models.CharField(max_length=13, unique=True)),
                ('description', models.TextField()),
                ('product_code', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('website', models.URLField(blank=True, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='puzzles', to='puzzle.company')),
                ('likes', models.ManyToManyField(related_name='puzzle_like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
