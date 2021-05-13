# Generated by Django 3.2.2 on 2021-05-13 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0003_space_variety'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='variety',
            field=models.CharField(choices=[('C', 'Car'), ('M', 'Motorcycle')], max_length=1),
        ),
    ]