# Generated by Django 3.2.7 on 2022-08-12 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rule1020', '0007_auto_20220812_1338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='economic',
            old_name='bel_15',
            new_name='below_15',
        ),
        migrations.RenameField(
            model_name='economic',
            old_name='eco_org',
            new_name='economic_organization',
        ),
        migrations.RenameField(
            model_name='economic',
            old_name='leg_org',
            new_name='legal_organization',
        ),
        migrations.RenameField(
            model_name='economic',
            old_name='main_eco',
            new_name='main_economic_activity',
        ),
        migrations.RenameField(
            model_name='economic',
            old_name='prod',
            new_name='major_producst',
        ),
        migrations.RenameField(
            model_name='economic',
            old_name='non_reg',
            new_name='non_regular',
        ),
        migrations.RenameField(
            model_name='economic',
            old_name='reg',
            new_name='regular',
        ),
        migrations.RenameField(
            model_name='economic',
            old_name='tot_emp',
            new_name='total_employment',
        ),
        migrations.RenameField(
            model_name='economic',
            old_name='subcon',
            new_name='total_number_of_subcontactors',
        ),
        migrations.RenameField(
            model_name='economic',
            old_name='subcon_emp',
            new_name='total_number_of_subcontracted_employees',
        ),
    ]
