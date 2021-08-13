from django.contrib import admin
from .models import Category
from .models import Images
from .models import Portfolio_projects
from .models import Skills
from .models import Experiences
from .models import Educations
from .models import About
from .models import Profile
from .models import Service
from .models import Testimonials
from .models import Contact
from .models import professions
from .models import Message
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']


@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    list_display=['MG','name']

@admin.register(Portfolio_projects)
class Portfolio_projectsAdmin(admin.ModelAdmin):
    list_display=['MG','name','title','thumbnail']

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display=['skill','image']

@admin.register(Experiences)
class ExperiencesAdmin(admin.ModelAdmin):
    list_display=['skill','image','company_name','company_logo','start_date','Posision','address','description','sk']


@admin.register(Educations)
class EducationsAdmin(admin.ModelAdmin):
    list_display=['skill','image','company_name','company_logo','start_date','Posision','address',
    'description','sk','Estart_date','end_date','institution_name',
    'institution_logo','education','CGPA','Out_Of','EX']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display=['skill','image','company_name','company_logo','start_date','Posision','address',
    'description','sk','Estart_date','end_date','institution_name','institution_logo','education',
    'CGPA','Out_Of','EX','ABOUT','cv_link','facebook_link','linkdin_link','github_link','AD']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name','ser_des','icon']


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ['client_name','company','speech','Tes_IMG']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['phone','email','CT_Add']


@admin.register(professions)
class professionsAdmin (admin.ModelAdmin):
    list_display=['profession']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display=['message']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['skill','image','company_name','company_logo','start_date','Posision','address',
    'description','sk','Estart_date','end_date','institution_name','institution_logo','education',
    'CGPA','Out_Of','EX','ABOUT','cv_link','facebook_link','linkdin_link','github_link','AD','firstname',
    'lastname','PD','MG','name','title','thumbnail','PP','service_name','ser_des','icon','SV','phone','email',
    'CT_Add','con_CT','client_name','company','speech','Tes_IMG','TMT','profession','PRO','message','ME']