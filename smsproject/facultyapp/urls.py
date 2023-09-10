
from django.urls import path
from .import views

urlpatterns = [

    path("checkfacultylogin", views.checkfacultylogin, name="checkfacultylogin"),
    path("facultyhome", views.facultyhome, name="facultyhome"),
    path("myfcourses",views.facultycourses,name="facultycourses"),

    path("facultychangepass", views.facultychangepass, name="facultychangepass"),
    path("facultyupdatepwd", views.facultyupdatepwd, name="facultyupdatepwd"),
    path("addcoursecontent", views.addcoursecontent, name="addcoursecontent"),


]