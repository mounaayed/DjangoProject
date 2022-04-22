from ast import Not
from django.urls import reverse
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.core.exceptions import ValidationError

# EmailValidator,MaxLengthValidator sinon on peut difinir des validator personalisé 


# Create your models here.
def emailValidator(email):
    if not str(email).endswith('@esprit.tn'):
        raise ValidationError("votre email est erronée") 
    return email

#if not '@' in email:

class User(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(verbose_name="Email",null=False,validators=[emailValidator])   #label : verbosename 
    def __str__(self) :
        return self.firstname +" " +self.lastname
    def get_absolute_url(self):
        return reverse('student_displayyyyyyyyy')
 
#fil table projet yekteb contenu firstname lastname


class Student(User):  #héritage
   pass   

class Supervisor(User):
    pass

class Project(models.Model): 
        name=models.CharField(max_length=50)
        duration=models.IntegerField()
        needs=models.TextField(max_length=250)
        timeallocated=models.IntegerField(validators=[MinValueValidator(2,"le templs min aloué doit etre =5")])
        description=models.TextField(max_length=250)
        Isvalid=models.BooleanField(default=False)
        Supervisor=models.ForeignKey(Supervisor,on_delete=models.SET_NULL,blank=True,null=True,related_name='project_sup') 
        creator=models.OneToOneField(Student,on_delete=models.CASCADE) 
        members=models.ManyToManyField(Student,related_name="lesmembers",blank=True,through="MembershipProject")
        def __str__(self) :
          return self.name +" " +str(self.duration)  #fil str héthi win table relation projet : esm w duration
        def __unicode__(self):
         return self.name
          
         #models.SET_NULL :ki tefasa5 supervisor yetfasa5ech projet
         #cascade :When the referenced object is deleted, also delete the objects that have references to it
        #blank : ya3ni required wala lé ,null ya3ni yeajem yekoun null
        #ForeignKey : manytoone
        #manytomany : fi wa7da barka tektebha
        #clé entragere m3a sstudent fil cours zedeha ,primary_key = True,
#through : bech declari table intermerdiare
        #fil onetoone params : primary_key = True

#The related_name attribute specifies the name of the reverse relation from the projet model back to your project.

class MembershipProject(models.Model):
    projet=models.ForeignKey(Project,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    time_allocated_by_member=models.IntegerField(validators=[MinValueValidator(2,"le templs min aloué doit etre =5")])
    

