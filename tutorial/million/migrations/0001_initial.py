# Generated by Django 2.2.6 on 2019-10-21 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('singer_sex', models.CharField(default='', max_length=20, verbose_name='Sex of singer')),
                ('singer_age', models.IntegerField(default='', verbose_name='Age of singer')),
                ('singer_style', models.CharField(default='', max_length=20, verbose_name='Style of singer')),
                ('singer_reputation', models.CharField(default='', max_length=20, verbose_name='Reputation of singer')),
                ('singer_price', models.CharField(default='', max_length=20, verbose_name='Price of singer')),
                ('owner', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='singer_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groups_style', models.CharField(default='', max_length=20)),
                ('groups_had', models.CharField(default='', max_length=20)),
                ('groups_songs', models.CharField(default='', max_length=20)),
                ('groups_diski', models.CharField(default='', max_length=20)),
                ('groups_singers', models.ManyToManyField(to='million.Singer')),
            ],
        ),
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Concert_date', models.CharField(default='', max_length=20, verbose_name='Concert date')),
                ('Concert_time', models.CharField(default='', max_length=20, verbose_name='Concert time')),
                ('Concert_place', models.CharField(default='', max_length=20, verbose_name='Concert place')),
                ('Concert_price', models.CharField(default='', max_length=20, verbose_name='Concert price')),
                ('Concert_name', models.CharField(default='', max_length=20, verbose_name='Concert name')),
                ('Concert_groups', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='million.Groups')),
            ],
        ),
    ]
