# Generated by Django 5.0.6 on 2024-06-06 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_member_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='license',
            field=models.ImageField(null=True, upload_to='member/license'),
        ),
        migrations.AlterField(
            model_name='member',
            name='profile_photo',
            field=models.ImageField(null=True, upload_to='member'),
        ),
    ]
