from django.db import models

# Create your models here.
class Category(models.Model):
    # cate_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, primary_key=True)


class Images(Category):
    cate = models.OneToOneField(Category, on_delete=models.CASCADE, parent_link=True)
    # img_id=models.AutoField(primary_key=True)
    MG = models.TextField()


class Portfolio_projects(Images):
    img = models.OneToOneField(Images, on_delete=models.CASCADE, parent_link=True)
    title = models.CharField(max_length=45)
    thumbnail = models.TextField()

class Skills(models.Model):
    skill=models.CharField(max_length=150,primary_key=True)
    image=models.TextField()

class Experiences(Skills):
    sk=models.OneToOneField(Skills, on_delete=models.CASCADE,parent_link=True)
    company_name=models.CharField(max_length=80,primary_key=True)
    company_logo=models.TextField()
    start_date=models.DateField()
    Posision=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    description=models.TextField()

class Educations(Experiences):
    EX=models.OneToOneField(Experiences, on_delete=models.CASCADE,parent_link=True)
    Estart_date=models.DateField()
    end_date=models.DateField()
    institution_name=models.CharField(max_length=45)
    institution_logo=models.TextField()
    education=models.CharField(max_length=25)
    CGPA=models.FloatField()
    Out_Of=models.FloatField()



class About(Educations):
    AD=models.OneToOneField(Educations, on_delete=models.CASCADE,parent_link=True)
    ABOUT=models.CharField(max_length=200,primary_key=True)
    cv_link=models.CharField(max_length=150)
    facebook_link=models.CharField(max_length=150)
    linkdin_link=models.CharField(max_length=150)
    github_link=models.CharField(max_length=150)

class Service(models.Model):
    service_name=models.CharField(max_length=35)
    ser_des=models.TextField()
    icon=models.TextField()


class Testimonials(models.Model):
    client_name=models.CharField(max_length=50,primary_key=True)
    company=models.CharField(max_length=60)
    speech=models.CharField(max_length=56)
    Tes_IMG=models.TextField()

class Contact(models.Model):
    phone=models.CharField(max_length=11,primary_key=True)
    email=models.EmailField()
    CT_Add=models.CharField(max_length=240)

class professions(models.Model):
    profession=models.CharField(max_length=70,primary_key=True)

class Message(models.Model):
    Mess_name=models.CharField(max_length=50)
    mess_email=models.EmailField(primary_key=True)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=80)

class Profile(About,Portfolio_projects,Service,Contact,Testimonials,professions,Message):
    PD=models.OneToOneField(About, on_delete=models.CASCADE,parent_link=True)
    PP=models.OneToOneField(Portfolio_projects, on_delete=models.CASCADE,parent_link=True)
    #CAT=models.OneToOneField(Contact, on_delete=models.CASCADE,parent_link=True)
    SV=models.OneToOneField(Service, on_delete=models.CASCADE,parent_link=True)
    con_CT = models.OneToOneField(Contact, on_delete=models.CASCADE, parent_link=True)
    TMT=models.OneToOneField(Testimonials, on_delete=models.CASCADE, parent_link=True)
    PRO=models.OneToOneField(professions, on_delete=models.CASCADE, parent_link=True)
    ME=models.OneToOneField(Message, on_delete=models.CASCADE, parent_link=True)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)