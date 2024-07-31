from django.db import models

# Create your models here.

class Scholarship(models.Model):
    image =models.ImageField(upload_to='images/', default="images/default.png")
    title= models.CharField(max_length=200)
    deadline = models.DateField()
    link = models.URLField()
    
    
    def __str__(self):
        return self.title
