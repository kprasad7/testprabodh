from django.urls import path
from student import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('studentclick', views.studentclick_view,name="studentclick"),
path('studentlogin', LoginView.as_view(template_name='student/studentlogin.html'),name='studentlogin'),
path('studentsignup', views.student_signup_view,name='studentsignup'),
path('student-dashboard', views.student_dashboard_view,name='student-dashboard'),
path('student-exam', views.student_exam_view,name='student-exam'),
path('take-exam/<int:pk>', views.take_exam_view,name='take-exam'),
path('start-exam/<int:pk>', views.start_exam_view,name='start-exam'),

path('calculate-marks', views.calculate_marks_view,name='calculate-marks'),
path('view-result', views.view_result_view,name='view-result'),
path('check-marks/<int:pk>', views.check_marks_view,name='check-marks'),
path('student-marks', views.student_marks_view,name='student-marks'),
path('student-video', views.video,name='video'),
path('student-pvideo', views.pvideo,name='pvideo'),

path('psviews', views.prabodhclassviewsv,name='pview'),
path('demovs' , views.demovsv , name="demov"),
path('demov1s' , views.demov1sv , name="demov1"),
path('demov2s' , views.demov2sv , name="demov2"),
path('demov3s' , views.demov3sv , name="demov3"),
path('demov4s' , views.demov4sv , name="demov4"),
path('demoviews/<int:pk>' , views.demoviewsv , name="demoview"),
path('demoview1s/<int:pk>' , views.demoview1sv , name="demoview1"),
path('demoview2s/<int:pk>' , views.demoview2sv , name="demoview2"),
path('demoview3s/<int:pk>' , views.demoview3sv , name="demoview3"),
path('demoview4s/<int:pk>' , views.demoviewsv , name="demoview4"),
path('futures/' , views.futuresv , name="future"),

path("complete/<task_id>", views.complete_task , name="complete"),
path("incomplete/<task_id>" , views.pending_task , name="incomplete"),


]