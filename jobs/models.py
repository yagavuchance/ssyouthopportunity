from django.db import models
from users.models import CustomUser
from ckeditor.fields import RichTextField

# Create your models here.

STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ]

class Jobs(models.Model):
    company = models.CharField(max_length=100)
    logo =models.ImageField(upload_to='images/',default='images/default.jpg')
    title = models.CharField(max_length=200)
    description = RichTextField( blank=True , null=True)
    location = models.CharField(max_length=100)
    deadline = models.DateField()
    description_file =models.FileField(upload_to='uploads', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='active')
    created_by =models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=True)

    def __str__(self):
        return self.title