from typing import DefaultDict
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image
from django.db.models.fields.related import ForeignKey
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete =models.CASCADE)
    profile_pic = models.ImageField(null=True,blank = True ,default = 'default.jpg')


    def __str__(self):
        return  self.user.username


    def save(self):
        super().save()

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)








    
    
 

