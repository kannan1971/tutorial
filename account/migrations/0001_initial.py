# Generated by Django 2.2.5 on 2019-11-13 12:59

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, verbose_name=django.contrib.auth.models.User)),
                ('description', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=10)),
                ('website', models.URLField(default='')),
                ('Phone', models.IntegerField(default=0)),
            ],
        ),
    ]
