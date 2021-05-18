# Generated by Django 3.2.2 on 2021-05-17 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='amount_paid',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='paid_at',
            field=models.DateField(null=True),
        ),
    ]
