# Generated by Django 3.1 on 2020-08-11 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyAPI', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardetails',
            old_name='Kmdriven',
            new_name='KM_driven',
        ),
    ]
