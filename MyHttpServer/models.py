from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100,null=False,blank=False)
    password=models.CharField(max_length=20,null=False,blank=False)
    
    def __unicode__(self):
        return self.username;
    
    
    
    def toDict(self):
        return dict(
                    id=self.id,
                    username=self.username,
                    password=self.password)
        
        
        
        
class CMMessage(models.Model):
    message = models.CharField(max_length=100)
    code = models.CharField(max_length=100,default="")
    
    def __unicode__(self):
        return self.message;
    
    
    def toDict(self):
        return dict(
                    id=self.id,
                    message=self.message,
                    code=self.code)
        

     