# Generated by Django 3.1 on 2020-09-21 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_books_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='Age',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
