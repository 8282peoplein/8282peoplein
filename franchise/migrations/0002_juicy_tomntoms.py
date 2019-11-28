# Generated by Django 2.2.3 on 2019-10-02 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('franchise', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Juicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='')),
                ('year', models.IntegerField()),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TomNToms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='')),
                ('year', models.IntegerField()),
                ('count', models.IntegerField()),
            ],
        ),
    ]
