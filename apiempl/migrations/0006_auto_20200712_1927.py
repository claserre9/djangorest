# Generated by Django 3.0.8 on 2020-07-12 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiempl', '0005_auto_20200712_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True),
        ),
    ]
