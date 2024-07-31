from django.db import models
from datetime import date

# Create your models here.
class Fellowship(models.Model):
    image= models.ImageField(upload_to='images/', default='images/default.png')
    title = models.CharField(max_length=100)
    deadline =models.DateField(default=date.today)
    link = models.URLField()
    
    
    def __str__(self):
        return self.title
    