# Generated by Django 5.0.7 on 2024-10-01 13:50

import users.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=users.utils.profile_image_upload),
        ),
    ]
