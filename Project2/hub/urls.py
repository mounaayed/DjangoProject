from django import views
from django.urls import path
from hub.views import ProjectLissstView, homePage, list_Student, detail_student, listprojet, addStudent, addstudentform, addstudentmodelformm, StudentCreateView, StudentUpdateView, StudentDeleteView, deletestudent, signup

urlpatterns = [
    path('home/', homePage, name="home"),
    path('student_display/', list_Student, name='student_displayyyyyyyyy'),
    path('detail/<int:id>', detail_student, name='detail_student'),
    path('projects/', listprojet, name='listprojet'),
    path('projectsvirw/', ProjectLissstView.as_view(), name='projectsvirw'),

    path('studentadd/', addStudent, name='studentadd'),

    path('studentaddjedida/', addstudentform, name='studentaddjedida'),

    path('studentaddjedida2/', addstudentmodelformm, name='studentaddjedida2'),
    path('studentaddjedida3/', StudentCreateView.as_view(),
         name='studentaddjedida3'),
    path('UpdateStudentView/<int:pk>',
         StudentUpdateView.as_view(), name='UpdateStudentView'),
    path('StudentDeleteView/<int:pk>',
         StudentDeleteView.as_view(), name='StudentDeleteView'),
    path('signup/', signup, name='signup'),

    path('deletestudent/<int:id>', deletestudent, name='deletestudent')



]

# Sometimes you want to name views so that you can refer to them by the name rather than by the url. That way,
# if the url changes in your app, you only need to update the code in one place //houni barka tebadel

    # path('deletestudent/<str:meta3sting>', deletestudent, name='deletestudent')
