from django.db import models

# Create your models here.

class Contact(models.Model):
    Name = models.CharField(max_length=100, blank=False)
    Email =models.EmailField(blank=False)
    message = models.TextField(max_length=150, blank=False)


    def __str__(self):
        return self.Email
