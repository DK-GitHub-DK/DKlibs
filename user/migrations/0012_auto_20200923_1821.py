# Generated by Django 3.1 on 2020-09-23 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='DatePayed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]