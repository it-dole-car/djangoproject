# Generated by Django 3.2.7 on 2022-08-12 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rule1020', '0010_alter_economic_tin_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='economic',
            name='total_number_of_subcontactors',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='economic',
            name='total_number_of_subcontracted_employees',
            field=models.IntegerField(),
        ),
    ]