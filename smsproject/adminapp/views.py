from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Admin,Course,Faculty,Student,FacultyCourseMapping
from .forms import AddFacultyForm, AddStudentForm,studentForm


# Create your views here.
def adminhome(request):
    auname=request.session["auname"]
    return render(request,"adminhome.html",{"adminuname":auname})

def logout(request):
    return render(request,"login.html")
def checkadminlogin(request):
    adminuname = request.POST["uname"]
    adminpwd=request.POST["pwd"]

    flag = Admin.objects.filter(Q(username=adminuname) & Q(password=adminpwd))
    print(flag)
    if flag:
        print("login success")
        request.session["auname"]=adminuname

        return render(request,'adminhome.html',{"adminuname":adminuname})
        #return HttpResponse("Login Success")
    else:
        msg="Login Failed"
        return render(request,"login.html",{"message":msg})



def viewstudents(request):
    students=Student.objects.all()
    count=Student.objects.count()
    auname = request.session["auname"]
    return render(request,"viewstudents.html",{"studentdata":students,"count":count,"adminuname":auname})
def viewfaculty(request):
    faculty=Faculty.objects.all()
    count = Faculty.objects.count()
    auname = request.session["auname"]
    return render(request,"viewfaculty.html",{"facultydata":faculty,"count":count,"adminuname":auname})
def viewcourse(request):
    courses=Course.objects.all()
    count =Course.objects.count()
    auname = request.session["auname"]
    return render(request,"viewcourse.html",{"coursedata":courses,"count":count,"adminuname":auname})
def adminchangepass(request):
    auname = request.session["auname"]

    return render(request,"adminchangepass.html",{"adminuname":auname})
def adminstudent(request):
    auname = request.session["auname"]

    return render(request,"adminstudent.html",{"adminuname":auname})
def adminfaculty(request):
    auname = request.session["auname"]

    return render(request,"adminfaculty.html",{"adminuname":auname})
def admincourse(request):
    auname = request.session["auname"]


    return render(request,"admincourse.html",{"adminuname":auname})
def addcourse(request):
    auname = request.session["auname"]

    return render(request,"addcourse.html",{"adminuname":auname})

def insertcourse(request):
    auname=request.session["auname"]
    if request.method=="POST":
        dept=request.POST["dept"]
        program=request.POST["program"]
        Academicyear=request.POST["Academicyear"]
        Semester=request.POST["Semester"]
        year=request.POST["year"]
        ccode=request.POST["ccode"]
        ctitle=request.POST["ctitle"]
        ltps=request.POST["ltps"]
        credits=request.POST["credits"]


        course=Course(department=dept,program=program,academicyear=Academicyear,semester=Semester,year=year,coursecode=ccode, coursetitle=ctitle,ltps=ltps,credits=credits)
        Course.save(course)
        message="Course added successfully"
        return render(request,'addcourse.html',{"msg":message,"adminuname":auname})
    else:
        message = "Failed to Add Student"
        return render(request, "addstudent.html", {"adminuname":auname,"msg":message})


def deletecourse(request):
    courses = Course.objects.all()
    count = Course.objects.count()
    auname = request.session["auname"]
    return render(request, "deletecourse.html", {"coursedata": courses, "count": count,"adminuname":auname})
def coursedeletion(request,cid):
    Course.objects.filter(id=cid).delete()
    return redirect("deletecourse")




def addfaculty(request):
    auname = request.session["auname"]
    form=AddFacultyForm()#non parameterised constructor
    if request.method=="POST":
        form1=AddFacultyForm(request.POST)
        if form1.is_valid():
            form1.save()#this will save inthe database table
            message="Faculty Added Successfully"
            #return HttpResponse("Facultu Added Successfully")
            return render(request, "addfaculty.html", {"msg": message, "form": form, "adminuname": auname})
        else:

            message = "Failed to Add Student"
            return render(request, "addstudent.html", {"form": form, "adminuname": auname, "msg": message})


    return render(request,"addfaculty.html",{"form":form,"adminuname":auname})

def deletefaculty(request):
    faculty = Faculty.objects.all()
    count = Faculty.objects.count()
    auname = request.session["auname"]
    return render(request, "deletefaculty.html", {"facultydata": faculty, "count": count,"adminuname":auname})
def facultydeletion(request,fid):
    Faculty.objects.filter(id=fid).delete()
    return redirect("deletefaculty")
def addstudent(request):
    auname = request.session["auname"]
    form=AddStudentForm()#non parameterised constructor
    if request.method=="POST":
        form1=AddStudentForm(request.POST)
        if form1.is_valid():
            form1.save()#this will save inthe database table
            message="Student Added Successfully"
            #return HttpResponse("Facultu Added Successfully"
            return render(request,"addstudent.html",{"msg":message,"form":form,"adminuname":auname})
        else:
            message = "Failed to Add Student"
            return render(request, "addstudent.html", {"form":form,"adminuname":auname,"msg":message})


    return render(request,"addstudent.html",{"form":form,"adminuname":auname})
def deletestudent(request):
    student = Student.objects.all()
    count = Student.objects.count()
    auname = request.session["auname"]
    return render(request, "deletestudent.html", {"studentdata": student, "count": count,"adminuname":auname})
def studentdeletion(request,sid):
    Student.objects.filter(id=sid).delete()
    return redirect("deletestudent")
def adminupdatepwd(request):
    auname = request.session["auname"]
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]
    flag=Admin.objects.filter(Q(username=auname)&Q(password=opwd))
    if flag:
        print("old pwd is correct")
        Admin.objects.filter(username=auname).update(password=npwd)
        print("updated sucess")
        msg="password updated successfully"
    else:
        print("old pwd is invalid")
        msg = "old pwd is invalid"

    return render(request,"adminchangepass.html",{"adminuname":auname,"message":msg})

def facultycoursemapping(request):
    fmcouses=FacultyCourseMapping.objects.all()

    auname=request.session["auname"]
    return render(request,"facultycoursemapping.html",{"adminuname":auname,"fmcourses":fmcouses})
def updatecourse(request):
    auname = request.session["auname"]

    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request,"updatecourse.html",{"adminuname":auname,"courses":courses,"count":count})
def courseupdation(request,cid):
    auname = request.session["auname"]
    return render(request,"courseupdation.html",{"cid":cid,"adminuname":auname})
def courseupdated(request):
    auname = request.session["auname"]
    cid=request.POST["cid"]
    courseid=int(cid)
    ctitle= request.POST["ctitle"]
    ltps= request.POST["ltps"]
    credits= request.POST["credits"]
    Course.objects.filter(id=courseid).update(coursetitle=ctitle,ltps=ltps,credits=credits)
    message="course updated successfully"
    return render(request,"courseupdation.html",{"msg":message,"adminuname":auname,"cid":cid})

def updatestudent(request):
    student = Student.objects.all()
    count = Student.objects.count()
    auname = request.session["auname"]
    return render(request, "updatestudent.html", {"studentdata": student, "count": count,"adminuname":auname})
def studentupdation(request,sid):
    auname=request.session["auname"]
    student=get_object_or_404(Student,pk=sid)
    if request.method == "POST":
        form=studentForm(request.POST,instance=student)


        if form.is_valid():
            form.save()  # this will save inthe database table
            return HttpResponse("Student Updated Successfully")
            # return HttpResponse("Facultu Added Successfully"

        else:
            return HttpResponse("Failed to Update Student")

    else:
        form=studentForm(instance=student)

    return render(request,"studentupdated.html",{"form":form,"adminuname":auname})



