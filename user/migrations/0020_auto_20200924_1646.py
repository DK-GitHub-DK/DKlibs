# Generated by Django 3.1 on 2020-09-24 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20200924_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
