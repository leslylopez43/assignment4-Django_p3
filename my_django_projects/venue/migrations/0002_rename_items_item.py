# Generated by Django 3.2.20 on 2023-08-07 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Items',
            new_name='Item',
        ),
    ]