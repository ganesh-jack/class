# Generated by Django 2.1.7 on 2020-08-01 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_tools'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='tools',
            new_name='tools_known',
        ),
    ]
