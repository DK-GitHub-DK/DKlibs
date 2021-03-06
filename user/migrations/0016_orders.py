# Generated by Django 3.1 on 2020-09-23 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_customer_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.customer')),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.books')),
            ],
        ),
    ]
