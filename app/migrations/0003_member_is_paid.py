# Generated by Django 5.0.6 on 2024-06-05 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_donation_options_alter_member_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
