# Generated by Django 2.2 on 2019-12-17 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdrm', '0004_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='image',
            field=models.CharField(default=None, max_length=256),
            preserve_default=False,
        ),
    ]