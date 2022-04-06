# Generated by Django 3.2.12 on 2022-04-06 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('custom_account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loggedinuser',
            name='session_key',
        ),
        migrations.AddField(
            model_name='loggedinuser',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sessions.session'),
        ),
    ]
