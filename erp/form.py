from django import forms
from django.db.models import fields
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CreateStudent(UserCreationForm):
    class Meta:
        model = Student
        fields = ('first_name', 'middle_name', 'last_name','roll_number', 'email', 'password1', 'password2')

class TakeProfilePic(forms.ModelForm):
    class Meta:
        model = Profile_pic
        fields = ('image', )

class hostel_leave_form(forms.ModelForm):
    class Meta:
        model = Hostel_Leave_Entry
        fields = ('academic_year', 'out_pass_type', 'out_pass_from', 'out_pass_to' , 'request_type', 'reason')


class request_form(forms.ModelForm):
    class Meta:
        model = Support_Request_form
        fields = ('category_name', 'description')
