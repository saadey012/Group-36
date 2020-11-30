from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class WebsiteUser(models.Model):
    user_id = models.CharField(null=True,blank=True,max_length=150,unique=True)
    user_name = models.CharField(null=True,blank=True,max_length=150)
    user_last_name = models.CharField(null=True,blank=True,max_length=150)
    user_address = models.CharField(null=True,blank=True,max_length=1000)
    user_phone = models.CharField(null=True,blank=True,max_length=1000)



    user_status = models.CharField(null=True,blank=True,max_length=150,choices=(('G',"Good"),('NG',"Not Good")))

    user_type  = models.CharField(null=True,blank=True, choices=(('A',"ADMIN"),('D',"DOCTOR") ,('P',"PATIENT")),max_length=400)
    user_password = models.CharField(null=True,blank=True,max_length=150)
    
    added = models.DateTimeField(auto_now=True)
    

   
            
    def __str__(self):
        return u'{0}'.format(self.user_id)