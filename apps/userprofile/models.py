from django.db import models
from django.contrib.auth.models import User

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile',on_delete=models.CASCADE)
    is_employer =  models.BooleanField(default = False)
    username = models.CharField(max_length=225,blank=True)
    fullname = models.CharField(max_length=225,blank=True,null=True)
    gender = models.CharField(max_length=225,blank=True,null=True)
    marital_status = models.CharField(max_length=225,blank=True,null=True)
    mobile = models.IntegerField(blank=True,null=True)
    email = models.EmailField(max_length=225,blank=True,null=True)
    alternate_email = models.EmailField(max_length=225,blank=True,null=True)
    skype_id = models.CharField(max_length=225,blank=True,null=True)
    alternate_contact = models.IntegerField(blank=True,null=True)
    imo_number = models.IntegerField(blank=True,null=True)
    address = models.CharField(max_length=225,blank=True,null=True)
    address = models.CharField(max_length=225,blank=True,null=True)
    district = models.CharField(max_length=225,blank=True,null=True)
    state = models.CharField(max_length=225,blank=True,null=True)
    pincode = models.IntegerField(blank=True,null=True)
    
    # territory = models.CharField(max_length=225,blank=True,null=True)
    # status = models.CharField(max_length=225,blank=True,null=True)
    # vacancies = models.CharField(max_length=225,blank=True,null=True)
    # qualification_type = models.CharField(max_length=225,blank=True,null=True)
    # specialization = models.CharField(max_length=225,blank=True,null=True)
    # category = models.CharField(max_length=225,blank=True,null=True)

User.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0])