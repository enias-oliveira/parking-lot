# Generated by Django 3.2.2 on 2021-05-13 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0002_rename_motorcylce_spaces_level_motorcycle_spaces'),
    ]

    operations = [
        migrations.AddField(
            model_name='space',
            name='variety',
            field=models.CharField(choices=[('car', 'car'), ('motorcycle', 'motorcycle')], default='car', max_length=255),
            preserve_default=False,
        ),
    ]
