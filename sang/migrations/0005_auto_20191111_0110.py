# Generated by Django 2.2.3 on 2019-11-10 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sang', '0004_sang_living_pop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sang',
            name='living_pop',
            field=models.IntegerField(null=True, verbose_name='거주인구 수'),
        ),
    ]
