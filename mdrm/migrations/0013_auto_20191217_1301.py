# Generated by Django 2.2 on 2019-12-17 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdrm', '0012_auto_20191217_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='ingredient',
            field=models.ManyToManyField(to='mdrm.Ingredient'),
        ),
    ]
