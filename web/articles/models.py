import uuid
from django.db import models
from django.urls import reverse

class Article(models.Model):
    id= models.UUIDField(
                        primary_key=True,
                        default=uuid.uuid4,
                        editable=False
                    )
    title= models.CharField(max_length=255)
    content= models.TextField()
    date= models.CharField(max_length=255,default="s")
    images= models.ImageField(upload_to="article_images/",blank=True,null=True)
    
    
    def __str__(self) -> str:
        return f"{self.title}"
    
    
    def get_absolute_url(self):
        return reverse("hello", kwargs={"pk": self.pk})
    
    
