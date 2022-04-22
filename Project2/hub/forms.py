from dataclasses import field, fields
from django import forms

from hub.models import Student

class StudentForm(forms.Form):
    firstname=forms.CharField(
         label="nommmm  ",
         max_length=50,



    )
    lastname=forms.CharField(
               
    )
    email=forms.EmailField()


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields ='__all__'
        help_texts = {'lastname':'hahahahaha'}