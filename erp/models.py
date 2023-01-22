from email.mime import application
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

import random

from django.db.models.expressions import Value

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, roll_number, email,first_name, middle_name, last_name, phone_number,application_number, uid, section, dob, course, admitted_through, applied_year, address, city, state, country, alternate_address, house_number, pincode, password=None):

        user=self.model(
            email=self.normalize_email(email),
            roll_number = roll_number,
            first_name = first_name,
            middle_name = middle_name,
            last_name = last_name,
            phone_number = phone_number,
            
            application_number = application_number,
            uid = uid,
            section = section,
            dob = dob,
            course = course,
            admitted_through = admitted_through,
            applied_year = applied_year,

            address = address,
            city = city,
            state = state,
            country = country,
            alternate_address = alternate_address,
            house_number = house_number,
            picode = pincode,
            # password = password,
#             # alternative_phone_number = alternative_phone_number,
#             # address = address,
#             # city = city,
#             # state=state,
#             # country = country,
#             # alternate_address = alternate_address,
#             # house_number = house_number,
#             # pincode = pincode
        )

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self,roll_number, email, first_name, middle_name, last_name, phone_number, password=None):
        user=self.create_user(
            email=email,
            roll_number = roll_number,
            first_name = first_name,
            middle_name = middle_name,
            last_name = last_name,
            phone_number = phone_number,
            password=password,
            # application_number= application_number,

        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class Student(AbstractBaseUser):
    first_name = models.CharField(verbose_name='First Name', max_length=200, null=True)
    middle_name = models.CharField(verbose_name='Middle Name', max_length=200, null=True)
    last_name = models.CharField(verbose_name='Last Name', max_length=200, null=True)
    phone_number = models.CharField(verbose_name='Phone Number', max_length=10, null=True)
    # alternative_phone_number = models.CharField(verbose_name='alternative_phone_number', max_length=10, null=True)
    roll_number = models.CharField(verbose_name='Roll Number', max_length=20, null=True, unique=True)
    application_number = models.CharField(verbose_name='Registration Number', max_length=20, null=True, unique=True)
    uid = models.CharField(verbose_name='UID', max_length=20, null=True)
    section = models.CharField(verbose_name='Section', max_length=20, null=True)
    dob = models.DateField(verbose_name='Date Of Birth', max_length=20, null=True)
    course = models.CharField(verbose_name='Course', max_length=200, null=True)
    admitted_through = models.CharField(verbose_name='Admitted Through', max_length=200, null=True)
    applied_year = models.CharField(verbose_name='Applied Year', max_length=20, null=True)
    address = models.CharField(verbose_name='address', max_length=500, null=True)
    city = models.CharField(verbose_name='city', max_length=200, null=True)
    state = models.CharField(verbose_name='state', max_length=200, null=True)
    country = models.CharField(verbose_name='country', max_length=100, null=True)
    alternate_address = models.CharField(verbose_name='alternate_address', max_length=500, null=True)
    house_number = models.CharField(verbose_name='house_number', max_length=5, null=True)
    pincode = models.CharField(verbose_name='pincode', max_length=10, null=True)

    email = models.EmailField(verbose_name='Email', max_length=60, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)



    USERNAME_FIELD = 'roll_number'
    # # REQUIRED_FIELDS = ['first_name']
    REQUIRED_FIELDS = ['first_name','middle_name', 'last_name', 'phone_number', 'email']

    objects = MyUserManager()

    def __str__(self):
        return self.roll_number


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class Profile_pic(models.Model):
    stu = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(null=True, blank=True) 

    def __str__(self):
        return self.stu.first_name + " " + self.stu.middle_name + " " + self.stu.last_name + "'s " + " Profile pic"

class Fee_details(models.Model):
    stu = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    year = models.CharField(max_length=200, null=True)
    total_amount = models.CharField(max_length=200, null=True)
    paid_amount = models.CharField(max_length=200, null=True)
    balance = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.stu.first_name + " " + self.stu.middle_name + " " + self.stu.last_name + "'s " + "Balance Amount: " +  self.balance

class Fee_Payment_History(models.Model):
    stu = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    receipt_number = models.IntegerField(null=True)
    receipt_date = models.DateField(null=True)
    amount = models.IntegerField(null=True)

    def __str__(self):
        return self.stu.first_name + " " + self.stu.middle_name + " " + self.stu.last_name + "'s " + "receipt number: " + str(self.receipt_number) + " Paid Amount: " +  str(self.amount)

Out_Pass_Type = (
    ('Medical', 'Medical'),
    ('Casual', 'Casual'),
    ('Festive', 'Festive'),
    # ('Thursday', 'Thursday'),
    # ('Friday', 'Friday'),
    # ('Saturday', 'Saturday'),
    # ('Sunday', 'Sunday'),
)

Academic_Year = (
    ('2013-2014', '2013-2014'),
    ('2014-2015', '2014-2015'),
    ('2015-2016', '2015-2016'),
    ('2016-2017', '2016-2017'),
    ('2017-2018', '2017-2018'),
    ('2019-2020', '2019-2020'),
    ('2020-2021', '2020-2021'),
    ('2021-2022', '2021-2022'),
)


Request_Type = (
    ('Parents Request', 'Parents Request'),
    ('Self Request', 'Self Request'),
    ('Both', 'Both'),
)

class Hostel_Leave_Entry(models.Model):
    academic_year = models.CharField(max_length=200, choices=Academic_Year)
    out_pass_type = models.CharField(max_length=20, choices=Out_Pass_Type)
    out_pass_from = models.DateField(null=True)
    out_pass_to = models.DateField(null=True)
    roll_number = models.CharField(verbose_name='roll_number', max_length=20, null=True)
    request_type = models.CharField(max_length=20, choices=Request_Type)
    reason = models.TextField(blank=True)

    def __str__(self):
        return self.roll_number + " " + self.reason

Category_Name = (
    ('Student Details Change', 'Student Details Change'),
    ('Attendance Related Issue', 'Attendance Related Issue'),
    ('Fee Related Issue', 'Fee Related Issue'),
    ('Other Issue', 'Other Issue'),
)

STATUS = (
        ('Pending', 'Pending'),
        ('In_Progress', 'In_Progress'),
        ('Resolved', 'Resolved'),
    )

Request_Id = random.randint(100, 999)

class Support_Request_form(models.Model):
    roll_number = models.CharField(verbose_name='roll_number', max_length=20, null=True)
    # stu = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    category_name = models.CharField(max_length= 50, choices=Category_Name)
    description = models.TextField(max_length = 200, blank=True)
    status = models.CharField(max_length=20, default="Pending", choices=STATUS)
    date_of_submission = models.DateField(null=True, auto_now=True)
    request_id = models.IntegerField(null=True, default=Request_Id)

    def __str__(self):
        return self.roll_number + "'s " + " Request"

class Subject(models.Model):
    # Student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    sub_name = models.CharField(max_length=200, null=True)
    sub_type = models.CharField(max_length=200, null=True)
    short_form = models.CharField(max_length=200, null=True)
    sub_code = models.CharField(max_length=200, null=True)
    conducted = models.IntegerField(null=True)
    # present = models.IntegerField(null=True)
    # total_hours_absent = models.IntegerField(null=True)
    # percentage = models.IntegerField(null=True)
    sub_id = models.IntegerField(null=True)
    def __str__(self):
        return self.short_form + " " + self.sub_type

class Student_Attendance(models.Model):
    stu = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    sub = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    present = models.IntegerField(null=True)
    total_hours_absent = models.IntegerField(null=True)
    percentage = models.IntegerField(null=True)

    def __str__(self):
        return self.stu.first_name + " " + self.stu.middle_name + " " + self.stu.last_name + " " + self.sub.short_form + " " + self.sub.sub_type

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)

Period = (
    ('1st', '1st'),
    ('2nd', '2nd'),
    ('3rd', '3rd'),
    ('4th', '4th'),
    ('5th', '5th'),
    ('6th', '6th'),
    ('7th', '7th'),
    ('8th', '8th'),
)

class Number_of_periods_absent(models.Model):
    stu = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    sub = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    number_of_periods_absent = models.IntegerField(null=True)
    def __str__(self):
        return str(self.number_of_periods_absent) + " " + "Periods Absent"



class Student_Absence_Details(models.Model):
    stu = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    sub = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    date = models.DateField(verbose_name='Date', max_length=20, null=True)
    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    which_period = models.CharField(max_length=20, choices=Period, null=True)
    def __str__(self):
        return self.stu.first_name + " " + self.stu.middle_name + " " + self.stu.last_name + " " + self.sub.short_form + " " + self.sub.sub_type + " " + "Absent in" + " " + self.which_period + " " + "period"
