# Generated by Django 4.0.3 on 2022-04-07 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0010_alter_support_request_form_request_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support_request_form',
            name='request_id',
            field=models.IntegerField(default=616, null=True),
        ),
    ]