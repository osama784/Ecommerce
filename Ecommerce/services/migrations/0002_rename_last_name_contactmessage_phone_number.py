# Generated by Django 5.0.7 on 2024-10-07 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmessage',
            old_name='last_name',
            new_name='phone_number',
        ),
    ]
