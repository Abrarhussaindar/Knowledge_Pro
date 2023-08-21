# Generated by Django 4.2.1 on 2023-08-21 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0013_alter_support_request_form_request_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='admitted_through',
        ),
        migrations.RemoveField(
            model_name='student',
            name='alternate_address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='application_number',
        ),
        migrations.RemoveField(
            model_name='student',
            name='applied_year',
        ),
        migrations.RemoveField(
            model_name='student',
            name='city',
        ),
        migrations.RemoveField(
            model_name='student',
            name='country',
        ),
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.RemoveField(
            model_name='student',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='student',
            name='house_number',
        ),
        migrations.RemoveField(
            model_name='student',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='student',
            name='section',
        ),
        migrations.RemoveField(
            model_name='student',
            name='state',
        ),
        migrations.RemoveField(
            model_name='student',
            name='uid',
        ),
        migrations.AlterField(
            model_name='support_request_form',
            name='request_id',
            field=models.IntegerField(default=583, null=True),
        ),
    ]