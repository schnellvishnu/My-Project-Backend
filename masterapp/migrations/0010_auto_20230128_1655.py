# Generated by Django 3.2.5 on 2023-01-28 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0009_auto_20230128_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='exp_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='manufacturing_date',
            field=models.DateField(null=True),
        ),
    ]
