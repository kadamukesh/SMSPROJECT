from django.db import models

# Create your models here.
class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,blank=False,unique=True)
    password= models.CharField(max_length=100, blank=False, unique=False)

    class Meta:
        db_table="admin_table"
    def __str__(self):
        return str(self.username)

class Course(models.Model):
    id = models.AutoField(primary_key=True)

    department_choices = (("Cse(Regular)", "Cse(R)"), ("Cse(Honorous)", "Cse(H)"), ("Cs&It", "CsIt"))
    department = models.CharField(max_length=100, blank=False,choices=department_choices)
    program_choices = (("Btech", "Btech"), ("Mtech", "Mtech"))
    program = models.CharField(max_length=10, blank=False, choices=program_choices)
    academicyear_choices=(("2023-24","2023-24"),("2022-23","2022-23"))
    academicyear=models.CharField(max_length=20, blank=False,choices=academicyear_choices)
    semester_choices = (("odd", "odd"),("Even", "Even"))
    semester = models.CharField(max_length=10,blank=False,choices=semester_choices)

    year = models.IntegerField(blank=False)
    coursecode = models.CharField(max_length=20, blank=False)
    coursetitle = models.CharField(max_length=100, blank=False)
    ltps= models.CharField(max_length=10, blank=False)
    credits=models.FloatField(blank=False)





    class Meta:
        db_table="course_table"
    def __str__(self):
        return str(self.coursecode)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    studentid=models.BigIntegerField(blank=False,unique=True)
    fullname= models.CharField(max_length=100, blank=False)
    gender_choices=(("Male","Male"),("Female","Female"),("Others","Others"))
    gender= models.CharField(max_length=20, blank=False,choices=gender_choices)
    department_choices = (("Cse(Regular)", "Cse(R)"), ("Cse(Honorous)", "Cse(H)"), ("Cs&It", "CsIt"))
    department = models.CharField(max_length=50, blank=False,choices=department_choices)
    program_choices=(("Btech","Btech"),("Mtech","Mtech"))
    program= models.CharField(max_length=10, blank=False,choices=program_choices)
    semester_choices = (("odd", "odd"), ("Even", "Even"))
    semester = models.CharField(max_length=20, blank=False,choices=semester_choices)
    year = models.IntegerField(blank=False)
    password= models.CharField(max_length=100, blank=False,default="klu123")
    email= models.CharField(max_length=100, blank=False,unique=True)
    pho= models.CharField(max_length=20, blank=False)
    aadharno=models.CharField(max_length=20, blank=False)




    class Meta:
        db_table="student_table"
    def __str__(self):
        return str(self.studentid)

class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    facultyid=models.BigIntegerField(blank=False,unique=True)
    fullname= models.CharField(max_length=100, blank=False)
    gender_choices = (("Male", "Male"), ("Female", "Female"), ("Others", "Others"))
    gender= models.CharField(max_length=20, blank=False,choices=gender_choices)
    department_choices = (("Cse(Regular)", "Cse(R)"), ("Cse(Honorous)", "Cse(H)"), ("Cs&It", "CsIt"))
    department = models.CharField(max_length=50, blank=False,choices=department_choices)
    qualification_choices = (("Btech", "Btech"), ("Mtech", "Mtech"),("PHD","PHD"))
    qualification= models.CharField(max_length=10, blank=False,choices=qualification_choices)
    designation_choices = (("prof", "professor"), ("Assoc proff", "Assoc proff"), ("Asst proff", "Asst proff"))
    designation= models.CharField(max_length=20, blank=False,choices=designation_choices)
    password= models.CharField(max_length=100, blank=False,default="klu123")
    email= models.CharField(max_length=100, blank=False)
    contact= models.CharField(max_length=20, blank=False,unique=True)


    class Meta:
        db_table="faculty_table"
    def __str__(self):
        return self.fullname

class FacultyCourseMapping(models.Model):
    mappingid=models.AutoField(primary_key=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    faculty= models.ForeignKey(Faculty, on_delete=models.CASCADE)
    component_choices=(("L","Lecture"),("T","Tutorial"),("P","Practical"),("S","Skill"))
    component=models.CharField(max_length=10,blank=False)
    type=models.BooleanField(blank=False,verbose_name="Facultytype")#true means main False mean Assistance faculty
    section=models.IntegerField(blank=False)
    class Meta:
        db_table="facultycoursemapping_table"
    def __str__(self):
        return f"{self.course.coursetitle}-{self.faculty.fullname}"
