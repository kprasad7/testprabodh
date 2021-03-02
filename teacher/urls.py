from django.urls import path
from teacher import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('teacherclick', views.teacherclick_view,name="teacherclick"),
path('teacherlogin', LoginView.as_view(template_name='teacher/teacherlogin.html'),name='teacherlogin'),
path('teachersignup', views.teacher_signup_view,name='teachersignup'),
path('teacher-dashboard', views.teacher_dashboard_view,name='teacher-dashboard'),
path('teacher-exam', views.teacher_exam_view,name='teacher-exam'),
path('teacher-add-exam', views.teacher_add_exam_view,name='teacher-add-exam'),
path('teacher-view-exam', views.teacher_view_exam_view,name='teacher-view-exam'),
path('delete-exam/<int:pk>', views.delete_exam_view,name='delete-exam'),


path('teacher-question', views.teacher_question_view,name='teacher-question'),
path('teacher-add-question', views.teacher_add_question_view,name='teacher-add-question'),
path('teacher-view-question', views.teacher_view_question_view,name='teacher-view-question'),
path('see-question/<int:pk>', views.see_question_view,name='see-question'),
path('remove-question/<int:pk>', views.remove_question_view,name='remove-question'),
path('utube', views.yuurlformm,name='yuurlformm'),
path('nutube', views.drivetubeurl,name='drivetubeurl'),
path('pvideo', views.pvideo,name='pvideo'),
path('uvideo', views.uvideo,name='uvideo'),
path('10thclass', views.tenurl,name='tenurl'),
path('9thclass', views.nineurl,name='nineurl'),
path('8thclass', views.eigurl,name='eigurl'),
path('7thclass', views.sevurl,name='sevurl'),
path('6thclass', views.sixurl,name='sixurl'),
path('lab1class', views.laburl,name='laburl'),
path('s1class', views.spurl,name='s1url'),
path('e1class', views.enurl,name='e1url'),
path('tview', views.teacherclassview,name='tview'),
path('pview', views.prabodhclassview,name='pview'),
path('p6view', views.p6video,name='p6video'),
path('demov' , views.demov , name="demov"),
path('demov1' , views.demov1 , name="demov1"),
path('demov2' , views.demov2 , name="demov2"),
path('demov3' , views.demov3 , name="demov3"),
path('demov4' , views.demov4 , name="demov4"),
path('demoview/<int:pk>' , views.demoview , name="demoviewsv"),
path('demoview1/<int:pk>' , views.demoview1 , name="demoview1"),
path('demoview2/<int:pk>' , views.demoview2 , name="demoview2"),
path('demoview3/<int:pk>' , views.demoview3 , name="demoview3"),
path('demoview4/<int:pk>' , views.demoview4 , name="demoview4"),
path('future/' , views.future , name="future"),




]