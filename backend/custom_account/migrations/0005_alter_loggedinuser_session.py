# Generated by Django 3.2.12 on 2022-04-07 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('custom_account', '0004_alter_loggedinuser_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loggedinuser',
            name='session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sessions.session'),
        ),
    ]