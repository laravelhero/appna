# Generated by Django 5.0.6 on 2024-06-04 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_donation_options_alter_member_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='license',
            field=models.ImageField(blank=True, null=True, upload_to='member/license'),
        ),
        migrations.AlterField(
            model_name='member',
            name='medical',
            field=models.CharField(choices=[('DMC', 'Dow Medical College'), ('SMC', 'Sindh Medical College'), ('AKMC', 'Aga Khan Medical College'), ('BMC', 'Bolan Medical College'), ('KMDC', 'Karachi Medical and Dental College'), ('ZMC', 'Ziauddin Medical College'), ('JMC', 'Jamshoro Medical College'), ('KEMC', 'King Edward Medical College'), ('AIMC', 'Allama Iqbal Medical College'), ('FJMC', 'Fatima Jinnah Medical College'), ('RMC', 'Rawalpindi Medical College'), ('NMC', 'Nishtar Medical College'), ('AMC', 'Ayub Medical College'), ('Others', 'Others')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='membership_type',
            field=models.CharField(choices=[(100, 'Lifetime Member ($100)')], default='Lifetime Member ($100)', max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='profile_photo',
            field=models.ImageField(blank=True, default='profile-pic.jpg', null=True, upload_to='member'),
        ),
    ]