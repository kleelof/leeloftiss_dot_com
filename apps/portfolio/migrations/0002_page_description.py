# Generated by Django 2.2 on 2019-12-26 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]