# Generated by Django 3.0.8 on 2020-07-12 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiempl', '0008_auto_20200712_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='profession',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
