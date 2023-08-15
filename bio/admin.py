from django.contrib import admin
from .models import Home,About,Resume,Contact,Social

class AdminHome(admin.ModelAdmin):
    list_display = ('title_owner','title_fixed','title_job','thumbnail','thumbnailbio','status')

admin.site.register(Home,AdminHome)


class AdminAbout(admin.ModelAdmin):
    list_display = ('description','des_title','des_title_des','des_detail','extra_des','thumbnailabout','status')

admin.site.register(About,AdminAbout)




class AdminResume(admin.ModelAdmin):
    list_display = ('project_owner','project_des','project_owner_title','description','status')
   
admin.site.register(Resume,AdminResume)





class AdminContact(admin.ModelAdmin):
    list_display = ('description','location','email','phone','age','degree','website','birthday','city','loc_pic','status')

admin.site.register(Contact,AdminContact)



class AdminSocial(admin.ModelAdmin):
    list_display = ('social_name','social_link','status')

admin.site.register(Social,AdminSocial)





# Register your models here.
