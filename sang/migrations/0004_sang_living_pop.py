# Generated by Django 2.2.3 on 2019-11-10 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sang', '0003_auto_20191109_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='sang',
            name='living_pop',
            field=models.IntegerField(null=True),
        ),
    ]