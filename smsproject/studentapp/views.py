from django.db.models import Q
from django.shortcuts import render

from adminapp.models import Student,Course
from facultyapp.models import CourseContent


# Create your views here.
def studenthome(request):
    sid=request.session["sid"]

    return render(request,"studenthome.html",{"sid":sid})

def checkstudentlogin(request):
    sid=request.POST["sid"]
    pwd=request.POST["pwd"]
    student = Student.objects.get(studentid=sid)
    print(student)

    flag=Student.objects.filter(Q(studentid=sid)&Q(password=pwd))
    print(flag)
    if flag:
        print("login success")
        request.session["sid"]=sid

        return render(request,'studenthome.html',{"sid":sid,"student":student})
        #return HttpResponse("Login Success")
    else:
        msg="Login Failed"
        return render(request,"studentlogin.html",{"message":msg})

def studentchangepass(request):
    sid=request.session["sid"]

    return render(request,"studentchangepass.html",{"sid":sid})
def studentupdatepwd(request):
    sid = request.session["sid"]
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]
    flag=Student.objects.filter(Q(studentid=sid)&Q(password=opwd))
    if flag:
        print("old pwd is correct")
        Student.objects.filter(studentid=sid).update(password=npwd)
        print("updated sucess")
        msg="password updated successfully"
    else:
        print("old pwd is invalid")
        msg= "old pwd is invalid"
    return render(request, "studentchangepass.html", {"sid": sid, "message": msg})

def studentcourses(request):
    sid=request.session["sid"]
    return render(request,"studentcourses.html",{"sid": sid})
def displaystudentcourses(request):
    sid=request.session["sid"]
    ay=request.POST["ay"]
    sem=request.POST["sem"]
    courses=Course.objects.filter(Q(academicyear=ay)&Q(semester=sem))
    return render(request,"displaystudentcourses.html",{"courses":courses,"sid": sid})
def studentcoursecontent(request):
    sid = request.session["sid"]
    content=CourseContent.objects.all()
    return render(request,"studentcoursecontent.html",{"sid":sid,"content":content})
