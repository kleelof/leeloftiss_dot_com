# Generated by Django 2.2 on 2019-12-19 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdrm', '0020_auto_20191218_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='allergens',
            field=models.ManyToManyField(null=True, related_name='profiles', to='mdrm.Allergen'),
        ),
    ]
