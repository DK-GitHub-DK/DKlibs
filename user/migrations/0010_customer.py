# Generated by Django 3.1 on 2020-09-23 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_books_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=200, null=True)),
                ('PhoneNo', models.CharField(max_length=200, null=True)),
                ('Email', models.CharField(max_length=200, null=True)),
                ('Address', models.CharField(max_length=10, null=True)),
                ('DatePayed', models.DateTimeField(null=True)),
            ],
        ),
    ]