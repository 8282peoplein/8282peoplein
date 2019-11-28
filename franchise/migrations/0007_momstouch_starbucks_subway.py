# Generated by Django 2.2.3 on 2019-10-04 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('franchise', '0006_auto_20191002_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Momstouch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('count', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'MOMSTOUCH',
            },
        ),
        migrations.CreateModel(
            name='Starbucks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('count', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'STARBUCKS',
            },
        ),
        migrations.CreateModel(
            name='Subway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('count', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'SUBWAY',
            },
        ),
    ]
