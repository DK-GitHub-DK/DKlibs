# Generated by Django 3.1 on 2020-09-23 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20200923_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='User',
        ),
    ]
