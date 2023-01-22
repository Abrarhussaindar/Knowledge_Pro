from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page, name="home"),
    path('', views.login_page, name="login"),
    path('cna/', views.create_new_customer, name="cna"),


    path('attendance/', views.attendance, name="attendance"),
    path('absence details/', views.absence_details, name="absence details"),
    path('previous attendance/', views.previous_attendance, name="previous attendance"),
    path('time table/', views.time_table, name="time table"),
    path('result/', views.result, name="result"),
    path('previous result/', views.previous_result, name="previous result"),
    path('view course plan/', views.view_course_plan, name="view course plan"),
    path('navbar/', views.navbar, name="navbar"),
    path('fee payment/', views.fee_payment, name="fee payment"),
    path('fee payment history/', views.fee_payment_history, name="fee payment history"),
    path('hostel leave entry/', views.hostel_leave_entry, name="hostel leave entry"),
    path('hostel leave entry form/', views.hostel_leave_entry_form, name="hostel leave entry form"),
    path('support/', views.support, name="support"),
    path('support request form/', views.support_request_form, name="support request form"),
    # path('course registration/', views.course_registration, name="course registration"),

]