from django.urls import path
from information.views import *
from django.contrib import admin


urlpatterns = [
    path('',index, name='index'),
    path('student/<slug:stud_id>/attendance/', attendance, name='attendance'),
    path('student/<slug:stud_id>/<slug:course_id>/attendance/', attendance_detail, name='attendance_detail'),
    path('student/<slug:class_id>/timetable/',timetable, name='timetable'),
    # path('student/<slug:class_id>/search/', views.student_search, name='student_search'),

    path('student/<slug:stud_id>/marks_list/', marks_list, name='marks_list'),

    path('teacher/<slug:teacher_id>/<int:choice>/Classes/',t_clas, name='t_clas'),
    path('teacher/<int:assign_id>/Students/attendance/', t_student, name='t_student'),
    path('teacher/<int:assign_id>/ClassDates/',t_class_date, name='t_class_date'),
    path('teacher/<int:ass_c_id>/Cancel/',cancel_class, name='cancel_class'),
    path('teacher/<int:ass_c_id>/attendance/',t_attendance, name='t_attendance'),
    path('teacher/<int:ass_c_id>/Edit_att/',edit_att, name='edit_att'),
    path('teacher/<int:ass_c_id>/attendance/confirm/',confirm, name='confirm'),
    path('teacher/<slug:stud_id>/<slug:course_id>/attendance/', t_attendance_detail, name='t_attendance_detail'),
    path('teacher/<int:att_id>/change_attendance/',change_att, name='change_att'),
    path('teacher/<int:assign_id>/Extra_class/',t_extra_class, name='t_extra_class'),
    path('teacher/<slug:assign_id>/Extra_class/confirm/', e_confirm, name='e_confirm'),
    path('teacher/<int:assign_id>/Report/',t_report, name='t_report'),

    path('teacher/<slug:teacher_id>/t_timetable/',t_timetable, name='t_timetable'),
    path('teacher/<int:asst_id>/Free_teachers/',free_teachers, name='free_teachers'),

    path('teacher/<int:assign_id>/marks_list/',t_marks_list, name='t_marks_list'),
    path('teacher/<int:assign_id>/Students/Marks/', student_marks, name='t_student_marks'),
    path('teacher/<int:marks_c_id>/marks_entry/',t_marks_entry, name='t_marks_entry'),
    path('teacher/<int:marks_c_id>/marks_entry/confirm/', marks_confirm, name='marks_confirm'),
    path('teacher/<int:marks_c_id>/Edit_marks/',edit_marks, name='edit_marks'),

]
admin.site.site_url= None
admin.site.site_header = 'My Site'
