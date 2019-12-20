# Generated by Django 2.2 on 2019-12-20 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pearako', '0009_auto_20191220_0927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='impages',
        ),
        migrations.AddField(
            model_name='projects',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='project', to='pearako.Image'),
        ),
    ]