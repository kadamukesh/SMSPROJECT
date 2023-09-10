from django.db.models import Q
from django.shortcuts import render

from adminapp.models import Faculty,FacultyCourseMapping,Course
from .forms import AddCourseContentForm




# Create your views here.

def checkfacultylogin(request):
    fid=request.POST["fid"]
    pwd=request.POST["pwd"]

    flag=Faculty.objects.filter(Q(facultyid=fid)&Q(password=pwd))
    print(flag)
    if flag:
        print("login success")
        request.session["fid"]=fid

        return render(request,'facultyhome.html',{"fid":fid})
        #return HttpResponse("Login Success")
    else:
        msg="Login Failed"
        return render(request,"facultylogin.html",{"message":msg})
def facultyhome(request):
    fid=request.session["fid"]
    return render(request,"facultyhome.html",{"fid":fid})
def facultycourses(request):
    fid = request.session["fid"]


    mappingcoursees=FacultyCourseMapping.objects.all()
    fmcourses=[]
    for course in mappingcoursees:
        if(course.faculty.facultyid==int(fid)):
            fmcourses.append(course)
    count=len(fmcourses)
    return render(request,"facultycourses.html",{"fid":fid,"fmcourses":fmcourses,"count":count})

def facultycoursemapping(request):
    fid = request.session["fid"]

    return render(request,"addcourse.html",{"fid":fid})
def facultychangepass(request):
    fid = request.session["fid"]

    return render(request,"facultychangepass.html",{"fid":fid})
def facultyupdatepwd(request):
    fid = request.session["fid"]
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]
    flag=Faculty.objects.filter(Q(facultyid=fid)&Q(password=opwd))
    if flag:
        print("old pwd is correct")
        Faculty.objects.filter(facultyid=fid).update(password=npwd)
        print("updated sucess")
        msg="password updated successfully"
    else:
        print("old pwd is invalid")
        msg = "old pwd is invalid"

    return render(request,"facultychangepass.html",{"fid":fid,"message":msg})
def addcoursecontent(request):
    fid = request.session["fid"]
   #non parameterised constructor
    if request.method=="POST":
        form2=AddCourseContentForm(request.POST)
        if form2.is_valid():
            form2.save()#this will save inthe database table
            message="CourseContent Added Successfully"
            #return HttpResponse("Facultu Added Successfully"
            return render(request,"addcoursecontent.html",{"msg":message,"form":form,"fid":fid})
        else:
            message = "Failed to Add CourseContent"
            return render(request, "addcoursecontent.html", {"form":form,"fid":fid,"msg":message})


    return render(request,"addcoursecontent.html",{"form":form,"fid":fid})

