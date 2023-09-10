from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render




def demofunc(request):
    return HttpResponse("<font color='red'><h1 align='center''>Welcome Mukesh<h1>")
def demofunc1(request):
    return HttpResponse("<h3>KLU</h3>")
def demofunc2(request):
    return HttpResponse("<font color='green'>Student Academic Management System</font>")
def homefunc(request):
    return render(request,"index.html")
def aboutfunc(request):
    return render(request,"about.html")
def loginfunc(request):
    return render(request,"login.html")

def contactfunc(request):
    return render(request, "contact.html")
def facultylogin(request):
    return render(request,"facultylogin.html")


def studentlogin(request):
    return render(request, "studentlogin.html")

