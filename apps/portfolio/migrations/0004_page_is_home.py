# Generated by Django 2.2 on 2019-12-26 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20191226_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='is_home',
            field=models.BooleanField(default=False),
        ),
    ]
