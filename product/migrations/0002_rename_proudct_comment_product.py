# Generated by Django 3.2.8 on 2021-10-09 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='proudct',
            new_name='product',
        ),
    ]
