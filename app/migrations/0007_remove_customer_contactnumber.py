# Generated by Django 3.2.7 on 2021-11-16 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_customer_contactnumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='contactnumber',
        ),
    ]
