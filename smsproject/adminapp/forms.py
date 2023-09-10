from django import forms
from .models import Faculty, Student


#add faculty will be created based on faculty model
class AddFacultyForm(forms.ModelForm):
    class Meta:
        model =Faculty #model name
        fields="__all__" #autp field will be hided
        exclude={"password"}# this will be exclude the fieldss
        labels={"facultyid":"Enter Faculty Id","gender":"Select Gender","fullname":"Enter full Name"} #to change name of the fields


class AddStudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        exclude = {"password"}  # this will be exclude the fieldss
        labels = {"studentid": "Enter Student Id", "gender": "Select Gender",
                  "fullname": "Enter full Name"}  # to change name of the fields


class studentForm(forms.ModelForm):
        class Meta:
            model = Student
            fields = "__all__"
            exclude = {"studentid"}