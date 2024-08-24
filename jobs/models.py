from django.db import models
from django.core.exceptions import ValidationError
from users.models import CustomUser
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils import timezone

# Define your allowed extensions
def validate_image_extension(value):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    ext = value.name.split('.')[-1].lower()
    if f'.{ext}' not in valid_extensions:
        raise ValidationError('Unsupported file extension.')

STATUS_CHOICES = [
    ('active', 'Active'),
    ('inactive', 'Inactive')
]


class Jobs(models.Model):
    company = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/', default='images/default.jpg', validators=[validate_image_extension])
    title = models.CharField(max_length=200)
    description = RichTextField(blank=True, null=True)
    location = models.CharField(max_length=100)
    deadline = models.DateField()
    description_file = models.FileField(upload_to='uploads', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)  # New field

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
       return reverse('description', args=[str(self.id)])
