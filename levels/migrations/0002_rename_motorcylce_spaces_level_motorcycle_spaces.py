# Generated by Django 3.2.2 on 2021-05-13 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='level',
            old_name='motorcylce_spaces',
            new_name='motorcycle_spaces',
        ),
    ]
