# Generated by Django 2.2 on 2019-12-17 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdrm', '0008_auto_20191217_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='allergens',
            field=models.ManyToManyField(blank=True, related_name='ingredients', to='mdrm.Allergen'),
        ),
    ]
