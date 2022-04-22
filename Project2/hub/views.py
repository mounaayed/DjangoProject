from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView,DeleteView,DetailView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Student
from .forms import StudentForm, StudentModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm



# Create your views here.


def homePage(request):
    return HttpResponse('<h1>hahahaha</h1>')

# if not user.is_authenticated:  // request.user.is_authenticated
#   ..........
# else:
    # ........ affichi page normal

@login_required
def list_Student(request):
    list = Student.objects.all()  # recuper tout les etudiant
    context = {
        'list_students': list,
    }
    return render(request, 'hub/list.html', {'list_students': list, }) #fil video 3adina context


def detail_student(request, id):
    student = Student.objects.get(id=id)  # get_object_or_404(Student,pk=id)
    return render(request, 'hub/details.html', {'student': student, })


def listprojet(request):
    list = Project.objects.all()  # recuper tout les etudiant

    return render(request, 'hub/listprojet.html', {'object_list': list})



class ProjectLissstView(LoginRequiredMixin,ListView):
    model = Project
    template_name = 'hub/listprojet.html'
    #ordering=['-name'] lil ordre
   # context_object_name.: bech tebadel esmeha ma3adech object_list
   # geenret une vue basé sur modele

def detail_student(request, id):
    student = Student.objects.get(id=id)  # get_object_or_404(Student,pk=id)
    return render(request, 'hub/details.html', {'student': student, })

def addStudent(request):
    # print(request.POST)
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")

        Student.objects.create(
            firstname=firstname,
            lastname=lastname,
            email=email

        )
        return redirect('student_displayyyyyyyyy')

    return render(request, 'hub/addstudent.html')


def addstudentform(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():

            Student.objects.create(

                firstname=form.cleaned_data.get('firstname'),

                lastname=form.cleaned_data['lastname'],

                email=form.cleaned_data['email']

            )
        return redirect('student_displayyyyyyyyy')

    return render(request, 'hub/addFormsss.html', {'form': form})


def addstudentmodelformm(request):
    form = StudentModelForm()

    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():

            student = form.save()
            return redirect('student_displayyyyyyyyy')

    return render(request, 'hub/addFormsss.html', {'form': form})


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    template_name = 'hub/addFormsss.html'


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm
    template_name = 'hub/addFormsss.html'
    success_url= reverse_lazy("student_displayyyyyyyyy")



class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'hub/Delete.html'
    success_url= reverse_lazy("student_displayyyyyyyyy")

def deletestudent(request,id):
    st=Student.objects.get(pk=id)
    st.delete()
    return redirect('student_displayyyyyyyyy')

# lezem yal9a form kilma fil html
# yarja3 wa7dou lil lien héthéké 3leh ?  w class meta chnowa héthika ?

#min 3andi 
def signup(request):
    if request.method =='POST':
        form=UserCreationForm(request.POST) #l envoi de la requette sera en mode post
        if form.is_valid():
            form.save()
            return redirect('student_displayyyyyyyyy')
    else:
         form=UserCreationForm()
    return render(request, 'hub/signup.html',{'f':form})