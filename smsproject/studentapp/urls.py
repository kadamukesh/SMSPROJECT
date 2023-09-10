from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views

urlpatterns = [
    path("checkstudentlogin", views.checkstudentlogin, name="checkstudentlogin"),

    path("studenthome", views.studenthome, name="studenthome"),
    path("studentcourses", views.studentcourses, name="studentcourses"),
    path("studentchangepass", views.studentchangepass, name="studentchangepass"),
    path("studentupdatepwd", views.studentupdatepwd, name="studentupdatepwd"),
    path("displayscourses",views.displaystudentcourses,name="displaystudentcourses"),
    path("studentcoursecontent ", views.studentcoursecontent, name="studentcoursecontent"),


]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)