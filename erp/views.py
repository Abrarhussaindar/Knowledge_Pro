from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .form import *
from .models import *
from django.http import JsonResponse
import json

# Create your views here.

def common_code(request):
    if request.user.is_authenticated:
        student = request.user
        # print("student",student)
        profile_imgs = Profile_pic.objects.filter(stu=student)
        if profile_imgs == {}:
            profile_imgs = ' '
    con = {
        'student': student,
        'profile_imgs': profile_imgs[0],
    }
    return con

def home_page(request):
    context1 = common_code(request)
    context = {
        'context1': context1,
    }
    return render(request, 'home.html',context)

def login_page(request):
    if request.method == 'POST':
        roll_number = request.POST.get('roll_number')
        password = request.POST.get('Password')
        # print(roll_number, password)
        student = authenticate(request, roll_number=roll_number, password=password)
        # print(student.is_authenticated)
        if student is not None:
            login(request, student)
            return redirect('home')
    context = {}
    return render(request, 'login_page.html',context)

def create_new_customer(request):
    form = CreateStudent()
    if request.method  == 'POST':
        form = CreateStudent(request.POST)
        # print(form.is_valid())
        # print(form.cleaned_data.get('email'))
        if form.is_valid():
            form.save()
            # print(form.cleaned_data.get('email'))
            return redirect('login')
    context = {'form': form}
    return render(request, 'cna.html', context)

def attendance(request):
    context1 = common_code(request)

    sub = Subject.objects.all()
    # print(sub)
    atten = Student_Attendance.objects.all()
    # print(atten[0].present)

    total_conducted = 0
    for i in range(0,1):
        total_conducted += sub[i].conducted
    # print(total_conducted)

    total_present = 0
    for i in range(0,1):
        total_present += atten[i].present
    #    print("total at "+ str(i) + " ", str(total_present))
    # print(total_present)

    total_absent_hours = 0
    for i in range(0,1):
        total_absent_hours += atten[i].total_hours_absent
    # print(total_absent_hours)

    total_percentage = 0
    for i in range(0,1):
        total_percentage += atten[i].percentage
    print(int(total_percentage/2))


    context = {
        'total_present': total_present,
        'total_conducted': total_conducted,
        'total_absent_hours': total_absent_hours,
        'total_percentage': int(total_percentage/2),
        'sub': sub,
        'atten': atten,
        'context1': context1,
    }
    return render(request, 'navigation/attendance.html', context)

def absence_details(request):
    context1 = common_code(request)
    student = request.user
    subs = Subject.objects.all()
    absen_details = Student_Absence_Details.objects.filter(stu=student)
    # print(absen_details)

    n_o_p_a = Number_of_periods_absent.objects.filter(stu=student)
    # print(n_o_p_a)

    total_periods = 0
    for i in range(0,len(n_o_p_a)):
        total_periods += n_o_p_a[i].number_of_periods_absent
    # print(int(total_periods))

    context = {
        'subs': subs,
        'absen_details': absen_details,
        'n_o_p_a': n_o_p_a,
        'total_periods': total_periods,
        'context1': context1,
    }
    return render(request, 'navigation/absence_details.html', context)

def previous_attendance(request):
    context1 = common_code(request)
    context = {
        'context1': context1,
    }
    return render(request, 'navigation/previous_attendance.html', context)

def time_table(request):
    context1 = common_code(request)
    context = {
        'context1': context1,
    }
    return render(request, 'navigation/time_table.html', context)

def navbar(request):
    context1 = common_code(request)
    # student = request.user
    # stu = Student.objects.filter(roll_number=student)
    # print('stu',stu)
    context = {
        # 'stu': stu,
        'context1': context1,
    }
    return render(request, 'navbar.html', context)


def result(request):
    context1 = common_code(request)
    context = {
        'context1': context1,
    }
    return render(request, 'navigation/result.html', context)

def previous_result(request):
    context1 = common_code(request)
    context = {
        'context1': context1,
    }
    return render(request, 'navigation/previous_result.html', context)

def view_course_plan(request):
    context1 = common_code(request)
    subs = Subject.objects.all()
    context = {
        'subs': subs,
        'context1': context1,
    }
    return render(request, 'navigation/view_course_plan.html', context)

# def download_course_plan(request, id):
#     sub = Subject.objects.filter(sub_id = id)
#     print(sub)
#     context1 = common_code(request)
#     context = {
#         'context1': context1,
#     }
#     return render(request, 'navigation/download_course_plan.html', context)



def fee_payment(request):
    context1 = common_code(request)
    student = request.user
    stu = Student.objects.filter(roll_number=student)
    # print("stu",stu)
    fees = Fee_details.objects.filter(stu=student)
    # print(fees)
    context = {
        'stu': stu,
        'fees': fees,
        'context1': context1,
    }
    return render(request, 'navigation/fee_payment.html', context)

def fee_payment_history(request):
    context1 = common_code(request)
    student = request.user
    stu = Student.objects.filter(roll_number=student)
    # print("stu",stu)
    fees = Fee_Payment_History.objects.filter(stu=student)
    # print(fees)

    total = 0
    for i in range(0,len(fees)):
        total += fees[i].amount
    # print(int(total))
    context = {
        'stu': stu,
        'fees': fees,
        'total': total,
        'context1': context1,
    }
    return render(request, 'navigation/fee_payment_history.html', context)

def hostel_leave_entry_form(request):
    context1 = common_code(request)

    form = hostel_leave_form()
    if request.method  == 'POST':
        form = hostel_leave_form(request.POST)


        print(form.is_valid())
        if form.is_valid():

            instance = form.save(commit=False)
            instance.roll_number = request.user
            # print(form.cleaned_data.get('email'))
            instance.save()
            # print(form.cleaned_data.get('email'))
            
            return redirect('hostel leave entry')


    context = {
        'form': form,
        'context1': context1,
    }
    return render(request, 'navigation/hostel_leave_entry_form.html', context)

def hostel_leave_entry(request):
    context1 = common_code(request)
    student = request.user
    form = Hostel_Leave_Entry.objects.filter(roll_number=student)
    # print(form)
    context = {
        'form': form,
        'context1': context1,
    }
    return render(request, 'navigation/hostel_leave_entry.html', context)

def support(request):
    context1 = common_code(request)
    student = request.user
    # print("roll_num",student)
    s_r = Support_Request_form.objects.filter(roll_number=student)
    # print(s_r)
    context = {
        's_r': s_r,
        'context1': context1,
    }
    return render(request, 'navigation/support.html', context)

def support_request_form(request):
    context1 = common_code(request)

    form = request_form()
    if request.method  == 'POST':
        form = request_form(request.POST)


        print(form.is_valid())
        if form.is_valid():

            instance = form.save(commit=False)
            instance.roll_number = request.user
            # print(form.cleaned_data.get('email'))
            instance.save()
            
            return redirect('support')


    context = {
        'form': form,
        'context1': context1,
    }
    return render(request, 'navigation/support_request_form.html', context)
