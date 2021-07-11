from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from quiz import models as QMODEL
from student import models as SMODEL
from quiz import forms as QFORM
from teddy.models import Video , extra , Drive
from teddy.forms import nurlform,yurlform
from .models import Teacher
from django.contrib import messages
from pclass.forms import sixform , sevform , eigform ,nineform , tenform , spform ,enform, labform
from pclass.models import sixth , sevennn , eightn , nine , tennn ,spnn , labbb ,envvv

#for showing signup/login button for teacher
def teacherclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'teacher/teacherclick.html')

def teacher_signup_view(request):
    userForm=forms.TeacherUserForm()
    teacherForm=forms.TeacherForm()
    mydict={'userForm':userForm,'teacherForm':teacherForm}
    if request.method=='POST':
        userForm=forms.TeacherUserForm(request.POST)
        teacherForm=forms.TeacherForm(request.POST,request.FILES)
        if userForm.is_valid() and teacherForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            teacher=teacherForm.save(commit=False)
            teacher.user=user
            teacher.save()
            my_teacher_group = Group.objects.get_or_create(name='TEACHER')
            my_teacher_group[0].user_set.add(user)
        return HttpResponseRedirect('teacherlogin')
    return render(request,'teacher/teachersignup.html',context=mydict)



def is_teacher(user):
    return user.groups.filter(name='TEACHER').exists()

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_dashboard_view(request):
    dict={
    
    'total_course':QMODEL.Course.objects.all().count(),
    'total_question':QMODEL.Question.objects.all().count(),
    'total_student':SMODEL.Studentt.objects.all().count(),
    'teachers':Teacher.objects.all().filter(status=True),
    }
    return render(request,'teacher/teacher_dashboard.html',context=dict)

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_exam_view(request):
    return render(request,'teacher/teacher_exam.html')


@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_add_exam_view(request):
    courseForm=QFORM.CourseForm()
    if request.method=='POST':
        courseForm=QFORM.CourseForm(request.POST)
        if courseForm.is_valid():        
            courseForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/teacher/teacher-view-exam')
    return render(request,'teacher/teacher_add_exam.html',{'courseForm':courseForm})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_view_exam_view(request):
    courses = QMODEL.Course.objects.all()
    return render(request,'teacher/teacher_view_exam.html',{'courses':courses})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def delete_exam_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/teacher/teacher-view-exam')

@login_required(login_url='adminlogin')
def teacher_question_view(request):
    return render(request,'teacher/teacher_question.html')

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_add_question_view(request):
    questionForm=QFORM.QuestionForm()
    if request.method=='POST':
        questionForm=QFORM.QuestionForm(request.POST)
        if questionForm.is_valid():
            question=questionForm.save(commit=False)
            course=QMODEL.Course.objects.get(id=request.POST.get('courseID'))
            question.course=course
            question.save()       
        else:
            print("form is invalid")
        return HttpResponseRedirect('/teacher/teacher-view-question')
    return render(request,'teacher/teacher_add_question.html',{'questionForm':questionForm})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_view_question_view(request):
    courses= QMODEL.Course.objects.all()
    return render(request,'teacher/teacher_view_question.html',{'courses':courses})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def see_question_view(request,pk):
    questions=QMODEL.Question.objects.all().filter(course_id=pk)
    return render(request,'teacher/see_question.html',{'questions':questions})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def remove_question_view(request,pk):
    question=QMODEL.Question.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect('/teacher/teacher-view-question')

##############################################################



        

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def yuurlformm(request):
    if request.method == "POST":
        form =  yurlform(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("form is invalid")  
        messages.success(request, 'successfully added video link')      
        return HttpResponseRedirect('utube')
    return render(request,'teacher/teacher-utube.html')

############################class form #########################
@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def tenurl(request):
    if request.method == "POST":
        form =  tenform(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("form is invalid")  
        messages.success(request, 'successfully added drive link')      
        return HttpResponseRedirect("10thclass")
    return render(request,'teacher/10utube.html')

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def nineurl(request):
    if request.method == "POST":
        form =  nineform(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("form is invalid")  
        messages.success(request, 'successfully added drive link')      
        return HttpResponseRedirect("9thclass")
    return render(request,'teacher/9utube.html')
@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def eigurl(request):
    if request.method == "POST":
        form =  eigform(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("form is invalid")  
        messages.success(request, 'successfully added drive link')      
        return HttpResponseRedirect("8thclass")
    return render(request,'teacher/8utube.html')
@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def sevurl(request):
    if request.method == "POST":
        form =  sevform(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("form is invalid")  
        messages.success(request, 'successfully added drive link')      
        return HttpResponseRedirect("7thclass")
    return render(request,'teacher/7utube.html')
@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def sixurl(request):
    if request.method == "POST":
        form =  sixform(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("form is invalid")  
        messages.success(request, 'successfully added drive link')      
        return HttpResponseRedirect("6thclass")
    return render(request,'teacher/6utube.html')
@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def laburl(request):
    if request.method == "POST":
        form =  labform(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("form is invalid")  
        messages.success(request, 'successfully added drive link')      
        return HttpResponseRedirect("lab1class")
    return render(request,'teacher/lab1.html')      
@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def spurl(request):
    if request.method == "POST":
        form =  spform(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("form is invalid")  
        messages.success(request, 'successfully added drive link')      
        return HttpResponseRedirect("s1class")
    return render(request,'teacher/s1utube.html') 
@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def enurl(request):
    if request.method == "POST":
        form =  enform(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("form is invalid")  
        messages.success(request, 'successfully added drive link')      
        return HttpResponseRedirect("e1class")
    return render(request,'teacher/e1utube.html')                             
###################################################################################
@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def drivetubeurl(request):
    if request.method == "POST":
        form =  nurlform(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("form is invalid")  
        messages.success(request, 'successfully added drive link')      
        return HttpResponseRedirect('nutube')
    return render(request,'teacher/teacher-nutube.html')    
###########################################################
@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def pvideo(request):
    data=Drive.objects.all()
    return render(request, 'teacher/teacher-pvideo.html',{'kk':data})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def uvideo(request):
    data=extra.objects.all()
    return render(request, 'teacher/teacher-uvideo.html',{'kkk':data})
##########################################################################view###########

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacherclassview(request):
    return render(request , "teacher/classmain.html")

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def prabodhclassview(request):
    return render(request , "teacher/prabodhclass.html")    
###################################################prabodh class view##################################    

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def p6video(request):
    data= sixth.objects.all()
    return render(request, 'teacher/p6view.html',{'mm':data})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def demov(request):
    data= sixth.objects.all()
    return render(request, 'teacher/demov.html',{'ml':data})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def demoview(request,pk):
    data = sixth.objects.all().filter(id=pk)
    return render(request,'teacher/demoview.html',{"qqq":data})
###########################################1################################
@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def demov1(request):
    data= sevennn.objects.all()
    return render(request, 'teacher/demov1.html',{'m1':data})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def demoview1(request,pk):
    data = sevennn.objects.all().filter(id=pk)
    return render(request,'teacher/demoview1.html',{"q1":data})    
#################################2#################################
@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def demov2(request):
    data= eightn.objects.all()
    return render(request, 'teacher/demov2.html',{'m2':data})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def demoview2(request,pk):
    data = eightn.objects.all().filter(id=pk)
    return render(request,'teacher/demoview2.html',{"q2":data})    
############################3###############################3###########
@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def demov3(request):
    data= nine.objects.all()
    return render(request, 'teacher/demov3.html',{'m3':data})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def demoview3(request,pk):
    data = nine.objects.all().filter(id=pk)
    return render(request,'teacher/demoview3.html',{"q3":data})    
##############################4####################################
@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def demov4(request):
    data= tennn.objects.all()
    return render(request, 'teacher/demov4.html',{'m4':data})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def demoview4(request,pk):
    data = tennn.objects.all().filter(id=pk)
    return render(request,'teacher/demoview4.html',{"q4":data})    
##################################future####################
def future(request):
   return render(request,'teacher/future.html')
###############################################################
def delete_task(request , task_id):
    if tennn.objects.filter(id=task_id).delete():
        messages.success(request, 'successfully deleted  object')
    else:
        messages.success(request, 'unsuccessfully deleted  object')
       
    return render(request,'teacher/demoview4.html')
    
        
      

    #task = tennn.objects.get(pk=task_id)  
    #if task.manage == request.user:
        #task.delete()
    #else:
        #messages.error(request,('Access Restricted You not allowed!'))

    #return render(request,'teacher/demoview4delete.html')  
    