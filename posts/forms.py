from django import forms
from jobs.models import Jobs
from ckeditor.widgets import CKEditorWidget

class JobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields =['company','logo','title','description','location','deadline','description_file','link']

        labels={
           'company': 'Organization',
           'logo': ' Upload Company Logo',
           'title': 'Job title',
           'description': 'Job Description',
           'location': 'Location',
           'deadline': 'Deadline',
           'description_file': 'Upload Job Description',
           'link': 'Upload job link '
        }

        widgets={
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter company name'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'upload company logo'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter job title'}),
            'description': CKEditorWidget(attrs={'class': 'form-control', 'placeholder': 'Enter job  description'}),
            'location':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter job location'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter application deadline'}),
            'description_file':forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'upload job dexcription'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'upload job link'}),
        }