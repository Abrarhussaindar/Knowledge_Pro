# Generated by Django 3.2.7 on 2022-02-04 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=200, null=True, verbose_name='first_name')),
                ('middle_name', models.CharField(max_length=200, null=True, verbose_name='middle_name')),
                ('last_name', models.CharField(max_length=200, null=True, verbose_name='last_name')),
                ('phone_number', models.CharField(max_length=10, null=True, verbose_name='phone_number')),
                ('roll_number', models.CharField(max_length=20, null=True, unique=True, verbose_name='roll_number')),
                ('application_number', models.CharField(max_length=20, null=True, unique=True, verbose_name='registration_number')),
                ('uid', models.CharField(max_length=20, null=True, verbose_name='uid')),
                ('section', models.CharField(max_length=20, null=True, verbose_name='section')),
                ('dob', models.DateField(max_length=20, null=True, verbose_name='dob')),
                ('admitted_through', models.CharField(max_length=200, null=True, verbose_name='admitted_through')),
                ('applied_year', models.CharField(max_length=20, null=True, verbose_name='applied_year')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hostel_Leave_Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_year', models.CharField(choices=[('2013-2014', '2013-2014'), ('2014-2015', '2014-2015'), ('2015-2016', '2015-2016'), ('2016-2017', '2016-2017'), ('2017-2018', '2017-2018'), ('2019-2020', '2019-2020'), ('2020-2021', '2020-2021'), ('2021-2022', '2021-2022')], max_length=200)),
                ('out_pass_type', models.CharField(choices=[('Medical', 'Medical'), ('Casual', 'Casual'), ('Festive', 'Festive')], max_length=20)),
                ('out_pass_from', models.DateField(null=True)),
                ('out_pass_to', models.DateField(null=True)),
                ('roll_number', models.CharField(max_length=20, null=True, verbose_name='roll_number')),
                ('request_type', models.CharField(choices=[('Parents Request', 'Parents Request'), ('Self Request', 'Self Request'), ('Both', 'Both')], max_length=20)),
                ('reason', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=200, null=True)),
                ('sub_type', models.CharField(max_length=200, null=True)),
                ('short_form', models.CharField(max_length=200, null=True)),
                ('sub_code', models.CharField(max_length=200, null=True)),
                ('conducted', models.IntegerField(null=True)),
                ('sub_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Support_Request_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.CharField(max_length=20, null=True, verbose_name='roll_number')),
                ('category_name', models.CharField(choices=[('Student Details Change', 'Student Details Change'), ('Attendance Related Issue', 'Attendance Related Issue'), ('Fee Related Issue', 'Fee Related Issue'), ('Other Issue', 'Other Issue')], max_length=50)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In_Progress', 'In_Progress'), ('Resolved', 'Resolved')], default='Pending', max_length=20)),
                ('date_of_submission', models.DateField(auto_now=True, null=True)),
                ('request_id', models.IntegerField(default=536, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('present', models.IntegerField(null=True)),
                ('total_hours_absent', models.IntegerField(null=True)),
                ('percentage', models.IntegerField(null=True)),
                ('stu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('sub', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='erp.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Absence_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=20, null=True, verbose_name='Date')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=10)),
                ('which_period', models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'), ('6th', '6th'), ('7th', '7th'), ('8th', '8th')], max_length=20, null=True)),
                ('stu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('sub', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='erp.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Profile_pic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('stu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Number_of_periods_absent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_periods_absent', models.IntegerField(null=True)),
                ('stu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('sub', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='erp.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Fee_Payment_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_number', models.IntegerField(null=True)),
                ('receipt_date', models.DateField(null=True)),
                ('amount', models.IntegerField(null=True)),
                ('stu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fee_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=200, null=True)),
                ('total_amount', models.CharField(max_length=200, null=True)),
                ('paid_amount', models.CharField(max_length=200, null=True)),
                ('balance', models.CharField(max_length=200, null=True)),
                ('stu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]