from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.username;
    
    
    
    def toDict(self):
        return dict(
                    id=self.id,
                    username=self.username,
                    password=self.password)
        

     