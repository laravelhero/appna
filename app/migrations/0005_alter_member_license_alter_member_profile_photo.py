# Generated by Django 5.0.6 on 2024-06-06 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_member_license_alter_member_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='license',
            field=models.ImageField(blank=True, null=True, upload_to='member/license'),
        ),
        migrations.AlterField(
            model_name='member',
            name='profile_photo',
            field=models.ImageField(blank=True, default='profile-pic.jpg', null=True, upload_to='member'),
        ),
    ]
