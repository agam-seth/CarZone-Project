# Generated by Django 3.0.7 on 2021-08-29 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20210829_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='old_price',
            field=models.IntegerField(default=0),
        ),
    ]