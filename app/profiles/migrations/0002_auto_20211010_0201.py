# Generated by Django 3.2.8 on 2021-10-10 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileclient',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profileseller',
            name='email',
        ),
    ]