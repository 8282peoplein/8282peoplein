# Generated by Django 2.2.3 on 2019-10-11 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forSale', '0002_auto_20191011_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Sector',
            new_name='sector',
        ),
    ]
