# Generated by Django 4.2.2 on 2023-08-20 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_token',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='otp_secret',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
