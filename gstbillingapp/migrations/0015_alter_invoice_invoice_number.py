# Generated by Django 3.2.6 on 2024-04-12 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20240412_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.IntegerField(unique=True),
        ),
    ]
