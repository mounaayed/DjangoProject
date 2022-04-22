from dataclasses import field, fields
from email import message
from pyexpat import model
import re
from django.contrib import admin,messages

from hub.models import MembershipProject, Project, Student, Supervisor, User

class ProdjectDurationFilter(admin.SimpleListFilter):
    title='duration ay 7aja'
    parameter_name="duration"
    def lookups(self, request, model_admin):
        return (('1 month',('less than 1 month')),
       ('3 month',('more  than 3 month')) )

    def queryset(self, request, queryset):
        if self.value()=='1 month':
            return queryset.filter(duration__lte=30)
        if self.value()=='3 month':
            return queryset.filter(duration__gte=30)

def set_Valid(modeladmin,request,queryset):
    rows_updated = queryset.update(Isvalid=True)
    if rows_updated==1:
        message="1 project was"
    else:
        message=f"{rows_updated} projects were"
    messages.success(request,message="%s successfully marked are valid"%message)
set_Valid.short_description="Validate"
#testgithub
# Register your models here.
  #ajouter table product bil crud fil partie admin
class projectinline(admin.TabularInline):
      model=Project
    #  fieldsets=[(None,{'fields':['name']})]  #fil ajout ajouti champ kol wala ken name
      extra=1  #9adeh min projet ye7otelek bech ajouti par default

class studentAdmin(admin.ModelAdmin):
    list_display=('lastname','firstname','email') #ordre
    fields=(('lastname','firstname'),'email')  #fard ligne ou nn (exclude : pour ne pas integrer un champ)
    inlines=[projectinline]

@admin.register(Supervisor)
class supervisorAdmin(admin.ModelAdmin):
    list_display=('lastname','firstname','email') #ordre
    search_fields=['lastname']  #teid 9ad ma te7eb champs 
    fields=(('lastname','firstname'),'email')  #fard ligne ou nn
    inlines=[projectinline]

class projectAdmin(admin.ModelAdmin):
    def set_noValidd(modeladmin,request,queryset):
        rows_updated = queryset.filter(Isvalid=False)
        if rows_updated.count()>0:
            messages.error(request,f"{rows_updated.count()} projects are marked as invalidddddd")
        else:
            rows_updated=queryset.update(Isvalid=False)
            if rows_updated==1:
                message="1 project was"
            else:
                message=f"{rows_updated} projects were"
            messages.success(request,message="%s successfully marked are invalid"%message)
    set_noValidd.short_description="Refuser"

    actions=[set_Valid,'set_noValidd']  #5ater wa7da de5el w wa7da bara
    actions_on_bottom=True
    actions_on_top=True

    list_display=('name','duration','Supervisor','creator')  # chnowa affichi
   # date_hierarchy='-updated_at'
  #  readonly_fields=('created_at')  #bech tegedech update predefinie read...

  #  radio_fields={"Supervisor":admin.VERTICAL}
    autocomplete_fields = ['Supervisor']
    list_filter=('creator','Isvalid',ProdjectDurationFilter)

    fieldsets=[
        ('state',{'fields':['Isvalid']}),
        ('about',{'fields':('name','duration','needs','Supervisor','timeallocated','description','creator')}),


     ] #organiser sous catogorie
    
     



admin.site.register(Student,studentAdmin)  

#admin.site.register(Supervisor,supervisorAdmin)  
admin.site.register(Project,projectAdmin)  
admin.site.register(MembershipProject)


