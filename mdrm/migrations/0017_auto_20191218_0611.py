# Generated by Django 2.2 on 2019-12-18 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdrm', '0016_auto_20191217_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverywindow',
            name='date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deliverywindow',
            name='close',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='deliverywindow',
            name='open',
            field=models.TimeField(),
        ),
    ]
