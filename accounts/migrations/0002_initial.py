# Generated by Django 4.0.4 on 2022-05-31 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('puzzle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='to_do',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_do', to='puzzle.puzzle'),
        ),
    ]