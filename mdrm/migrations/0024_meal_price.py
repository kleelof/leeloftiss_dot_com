# Generated by Django 2.2 on 2019-12-19 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdrm', '0023_auto_20191218_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
