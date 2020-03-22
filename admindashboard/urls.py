from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/admin-dashboard.html', views.admindashboard),
    path('dashboard/admin-add-student.html', views.admin_add_student),
    path('dashboard/admin-student-list.html', views.admin_studentlist),
    path('dashboard/admin-add-teacher.html', views.admin_add_teacher),
    path('dashboard/admin-teacher-list.html', views.admin_teacherlist),
    path('dashboard/message.html', views.admin_messages),
    path('dashboard/admin-add-announcement.html', views.admin_add_announcement),
    path('dashboard/admin-add-class.html', views.admin_add_class),
    path('dashboard/admin-add-section.html', views.admin_add_section),
    path('dashboard/admin-add-subject.html', views.admin_add_subject),
    path('dashboard/admin-create-timetable.html', views.admin_create_timetable),
    path('dashboard/admin-class-timetable.html', views.admin_class_tintetable),
    path('dashboard/teacher-attendence-report.html', views.admin_attendace),
    path('dashboard/teacher-marks-report.html', views.admin_marks),

]