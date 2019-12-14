# Generated by Django 2.2 on 2019-12-14 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('the_ask', models.TextField(blank=True)),
                ('challenges', models.TextField(blank=True)),
                ('solution', models.TextField(blank=True)),
                ('github_link', models.CharField(blank=True, max_length=256)),
                ('external_link', models.CharField(blank=True, max_length=256)),
                ('show_on_home', models.BooleanField(default=False)),
                ('show_n_jewels', models.BooleanField(default=False)),
                ('technologies', models.ManyToManyField(related_name='projects', to='pearako.Technologies')),
            ],
        ),
    ]
