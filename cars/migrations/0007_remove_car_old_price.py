# Generated by Django 3.0.7 on 2021-08-29 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_auto_20210829_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='old_price',
        ),
    ]