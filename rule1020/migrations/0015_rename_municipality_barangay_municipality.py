# Generated by Django 3.2.7 on 2022-08-15 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rule1020', '0014_auto_20220815_1313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='barangay',
            old_name='Municipality',
            new_name='municipality',
        ),
    ]