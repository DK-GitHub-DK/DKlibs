# Generated by Django 3.1 on 2020-09-24 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_auto_20200924_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='recieved_on',
            field=models.DateField(blank=True, null=True),
        ),
    ]