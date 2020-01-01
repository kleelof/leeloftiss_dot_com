# Generated by Django 2.2 on 2019-12-26 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_page_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='show_on_bootcamp',
        ),
        migrations.RemoveField(
            model_name='project',
            name='show_on_home',
        ),
        migrations.RemoveField(
            model_name='project',
            name='show_on_jewels',
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(help_text='Enter the FULL name of the file', max_length=256),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.CharField(help_text='use_underscores', max_length=100),
        ),
    ]