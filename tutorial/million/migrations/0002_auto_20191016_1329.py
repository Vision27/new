# Generated by Django 2.2.6 on 2019-10-16 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('million', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Concert_date', models.CharField(default='', max_length=20, verbose_name='kek')),
                ('Concert_time', models.CharField(default='', max_length=20, verbose_name='kek')),
                ('Concert_place', models.CharField(default='', max_length=20, verbose_name='kek')),
                ('Concert_price', models.CharField(default='', max_length=20, verbose_name='kek')),
                ('Concert_ft', models.CharField(default='', max_length=20, verbose_name='kek')),
                ('Concert_name', models.CharField(default='', max_length=20, verbose_name='kek')),
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
            ],
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('singer_sex', models.CharField(default='', max_length=20, verbose_name='kek')),
                ('singer_age', models.IntegerField(default='', verbose_name='kek')),
                ('singer_style', models.CharField(default='', max_length=20, verbose_name='kek')),
                ('singer_reputation', models.CharField(default='', max_length=20, verbose_name='kek')),
                ('singer_prize', models.CharField(default='', max_length=20, verbose_name='kek')),
            ],
        ),
        migrations.DeleteModel(
            name='sex',
        ),
        migrations.AddField(
            model_name='groups',
            name='groups_singers',
            field=models.ManyToManyField(to='million.Singer'),
        ),
        migrations.AddField(
            model_name='concert',
            name='Concert_groups',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='million.Groups'),
        ),
    ]