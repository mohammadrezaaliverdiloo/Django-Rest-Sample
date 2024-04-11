from django.db import models

class article(models.Model):
    title= models.CharField(max_length=255)
    content= models.TextField()
    date=models.CharField(max_length=255,default="s")
    
