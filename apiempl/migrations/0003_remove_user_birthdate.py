# Generated by Django 3.0.8 on 2020-07-11 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiempl', '0002_auto_20200710_2155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthdate',
        ),
    ]
