# Generated by Django 2.2 on 2019-12-18 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mdrm', '0017_auto_20191218_0611'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='deliverywindow',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_window',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='mdrm.DeliveryWindow'),
        ),
        migrations.AddField(
            model_name='order',
            name='meal',
            field=models.ManyToManyField(related_name='order', to='mdrm.Meal'),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'pending'), (2, 'canceled'), (3, 'completed'), (4, 'assembling')], default=4),
        ),
    ]
