# Generated by Django 3.2.7 on 2022-08-12 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rule1020', '0004_rename_info_emp'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp',
            name='mun',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
