# Generated by Django 3.0.8 on 2020-07-12 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiempl', '0003_remove_user_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
