from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from datetime import datetime



# Create your models here.
class TutorDetail(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    contact=models.CharField(max_length=15, null=True)
    gender=models.CharField(max_length=50, null=True)
    date=models.DateField(null=True)


 


class Item(models.Model):
    video = EmbedVideoField()


class Data(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)


    def __str__(self):
        return self.location

class tutorreg(models.Model):
    name = models.CharField(max_length=100)
    NID=models.IntegerField(max_length=17)
    Address=models.CharField(max_length=100)
    SSCDiv=models.CharField(max_length=10)
    SSCyr=models.IntegerField(max_length=10)
    SSCres=models.FloatField(max_length=4)
    SSCinst=models.CharField(max_length=100)
    HSCDiv=models.CharField(max_length=10)
    HSCyr=models.IntegerField(max_length=10)
    HSCres=models.FloatField(max_length=4)
    HSCinst=models.CharField(max_length=100)
    UNDRsub=models.CharField(max_length=100,null=True)
    UNDRyr=models.IntegerField(max_length=10,null=True)
    UNDRres=models.FloatField(max_length=4,null=True)
    UNDRinst=models.CharField(max_length=100,null=True)
   
    def __str__(self):
        return self.name
    
class tutorreg2(models.Model):
    name = models.CharField(max_length=100)
    NID=models.IntegerField()
    primary=models.CharField(max_length=10)
    junior_secondary=models.CharField(max_length=10)
    secondary=models.CharField(max_length=10)
    hsc=models.CharField(max_length=10)
    undergrade=models.CharField(max_length=10)
    postgrade=models.CharField(max_length=10)
    area=models.CharField(max_length=15)
    experiance=models.IntegerField()
    image=models.ImageField()
    mobile=models.IntegerField()

    def __str__(self):
        return self.name

class addtutor(models.Model):
    stdname=models.CharField(max_length=100)
    tcrname=models.CharField(max_length=100)
    mobile=models.IntegerField()
    satrtDate=models.DateField()
    payment=models.IntegerField()
    area=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.tcrname
    
    
class Payment(models.Model):
    
    tcrname=models.CharField(max_length=100)
    mobile=models.IntegerField()
    stdname=models.CharField(max_length=100)
    payment=models.IntegerField()

    def __str__(self):
        return self.stdname
    
    

class attendence(models.Model):
    stdname=models.CharField(max_length=100)
    tcrname=models.CharField(max_length=100)
    attendence=models.IntegerField()

    def __str__(self):
        return self.stdname

    
class notification1(models.Model):
    tchrname=models.CharField(max_length=100)
    stdname=models.CharField(max_length=100)
    stdname_last=models.CharField(max_length=100,null=True)
    stdemail=models.CharField(max_length=100)
    contact=models.IntegerField(null=True)
    Area=models.CharField(max_length=100,null=True)
    tcrname=models.CharField(max_length=100)
    date=models.DateField()
    pay=models.IntegerField()  
    
    def __str__(self):
        return self.tchrname

class personaltutor(models.Model):
    stdname=models.CharField(max_length=100)
    tchrname=models.CharField(max_length=100)
    Starting_Date=models.DateField()
    payment=models.IntegerField()
    Status=models.CharField(max_length=100,default='Due')
    attendence=models.IntegerField(default=0)
    def __str__(self):
        return self.stdname
    

class Room(models.Model):
    name = models.CharField(max_length=10000)

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)