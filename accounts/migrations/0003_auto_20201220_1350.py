# Generated by Django 3.0.7 on 2020-12-20 10:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_profil_profile_pic'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profil',
            new_name='Customer',
        ),
    ]