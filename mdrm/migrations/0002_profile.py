# Generated by Django 2.2 on 2019-12-15 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdrm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=100)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=25)),
                ('allergens', models.ManyToManyField(related_name='profiles', to='mdrm.Allergens')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]