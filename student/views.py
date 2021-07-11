from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from quiz import models as QMODEL
from teacher import models as TMODEL
from student import models as SMODEL
from teddy.forms import yurlform
from teddy.models import Item, Drive , extra
from lvid.models import Itemm
from pclass.models import sixth , sevennn , eightn , nine , tennn ,spnn , labbb ,envvv
from django.contrib import messages

def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'student/studentclick.html')
    

def student_signup_view(request):
    userForm=forms.StudentUserForm()
    studentForm=forms.StudentForm()
    mydict={'userForm':userForm,'studentForm':studentForm}
    if request.method=='POST':
        userForm=forms.StudentUserForm(request.POST)
        studentForm=forms.StudentForm(request.POST,request.FILES)
        if userForm.is_valid() and studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            student=studentForm.save(commit=False)
            student.user=user
            student.save()
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        return HttpResponseRedirect('studentlogin')
    return render(request,'student/studentsignup.html',context=mydict)

def is_student(user):
    return user.groups.filter(name='STUDENT').exists()

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_dashboard_view(request):
    dict={
    
    'total_course':QMODEL.Course.objects.all().count(),
    'total_question':QMODEL.Question.objects.all().count(),
    "stud":SMODEL.Studentt.objects.get(user_id=request.user.id),
    }
    return render(request,'student/student_dashboard.html',context=dict)

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_exam_view(request):
    
    dict={
        "courses":QMODEL.Course.objects.all(),
        "stud":SMODEL.Studentt.objects.get(user_id=request.user.id)
        
    }
    return render(request,'student/student_exam.html',context=dict)

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def take_exam_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    total_questions=QMODEL.Question.objects.all().filter(course=course).count()
    questions=QMODEL.Question.objects.all().filter(course=course)
    stud=SMODEL.Studentt.objects.get(user_id=request.user.id)
    total_marks=0
    for q in questions:
        total_marks=total_marks + q.marks
    
    return render(request,'student/take_exam.html',{'course':course,'total_questions':total_questions,'total_marks':total_marks,"stud":stud})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def start_exam_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    questions=QMODEL.Question.objects.all().filter(course=course)
    stud=SMODEL.Studentt.objects.get(user_id=request.user.id)
    if request.method=='POST':
        pass
    response= render(request,'student/start_exam.html',{'course':course,'questions':questions,"stud":stud})
    response.set_cookie('course_id',course.id)
    return response


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def calculate_marks_view(request):

    if request.COOKIES.get('course_id') is not None:
        course_id = request.COOKIES.get('course_id')
        course=QMODEL.Course.objects.get(id=course_id)
        
        total_marks=0
        questions=QMODEL.Question.objects.all().filter(course=course)
        for i in range(len(questions)):
            
            selected_ans = request.COOKIES.get(str(i+1))
            actual_answer = questions[i].answer
            if selected_ans == actual_answer:
                total_marks = total_marks + questions[i].marks
        student = models.Studentt.objects.get(user_id=request.user.id)
        result = QMODEL.Result()
        result.marks=total_marks
        result.exam=course
        result.student=student
        result.save()
        return HttpResponseRedirect('view-result')
    


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def view_result_view(request):
    dict={
        "courses":QMODEL.Course.objects.all(),
        "stud":SMODEL.Studentt.objects.get(user_id=request.user.id)

    }
    return render(request,'student/view_result.html',context=dict)
    

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def check_marks_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    student = models.Studentt.objects.get(user_id=request.user.id)
    results= QMODEL.Result.objects.all().filter(exam=course).filter(student=student)
    stud=SMODEL.Studentt.objects.get(user_id=request.user.id)
    return render(request,'student/check_marks.html',{'results':results,"stud":stud})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_marks_view(request):
    courses=QMODEL.Course.objects.all()
    stud=SMODEL.Studentt.objects.get(user_id=request.user.id)
    return render(request,'student/student_marks.html',{'courses':courses,"stud":stud})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def video(request):
    data=extra.objects.all()
    stud=SMODEL.Studentt.objects.get(user_id=request.user.id)
    return render(request, 'student/student-video.html',{'klk':data,"stud":stud})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def pvideo(request):
    data =Drive.objects.all()
    stud=SMODEL.Studentt.objects.get(user_id=request.user.id)
    return render(request, 'student/student-pvideo.html',{'kk':data,"stud":stud})    

#################################################################################

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def prabodhclassviewsv(request):
    return render(request , "student/classmains.html")    
###################################################prabodh class view##################################    

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def demovsv(request):
    data= sixth.objects.all()
    return render(request, 'student/demovs.html',{'mls':data})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def demoviewsv(request,pk):
    data = sixth.objects.all().filter(id=pk)
    return render(request,'student/demoviews.html',{"qqqs":data})
###########################################1################################
@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def demov1sv(request):
    data= sevennn.objects.all()
    return render(request, 'student/demov1s.html',{'m1s':data})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def demoview1sv(request,pk):
    data = sevennn.objects.all().filter(id=pk)
    return render(request,'student/demoview1s.html',{"q1s":data})    
#################################2#################################
@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def demov2sv(request):
    data= eightn.objects.all()
    return render(request, 'student/demov2s.html',{'m2s':data})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def demoview2sv(request,pk):
    data = eightn.objects.all().filter(id=pk)
    return render(request,'student/demoview2s.html',{"q2s":data})    
############################3###############################3###########
@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def demov3sv(request):
    data= nine.objects.all()
    return render(request, 'student/demov3s.html',{'m3s':data})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def demoview3sv(request,pk):
    data = nine.objects.all().filter(id=pk)
    return render(request,'student/demoview3s.html',{"q3s":data})    
##############################4####################################
@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def demov4sv(request):
    data= tennn.objects.all()
    return render(request, 'student/demov4s.html',{'m4s':data})


def demoview4sv(request,pk):
    data = tennn.objects.all().filter(id=pk)
    return render(request,'student/demoview4s.html',{"q4s":data}) 

def futuresv(request):
   return render(request,'student/futures.html')
###################################################################################


################################################################################    

def complete_task(request , task_id):
    task = sixth.objects.get(pk=task_id) 
    if task.six == request.user:
        task.done = True
        task.save()
    else: 
         messages.error(request,('Access Restricted You not allowed!')) 
    
    return redirect('demov' , {"mkk":task})

def pending_task(request , task_id):
    task = sixth.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('demov')    