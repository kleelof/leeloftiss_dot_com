# Generated by Django 2.2 on 2019-12-17 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdrm', '0009_auto_20191217_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.SmallIntegerField(choices=[(1, 'oz'), (2, 'fl oz'), (3, 'ea')], default=1),
        ),
    ]
