from django import forms
from jobs.models import Jobs
from scholarship.models import Scholarship
from ckeditor.widgets import CKEditorWidget

class JobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['company', 'logo', 'title', 'description', 'location', 'deadline', 'description_file', 'link']

        labels = {
            'company': 'Organization',
            'logo': 'Upload Company Logo',
            'title': 'Job title',
            'description': 'Job Description',
            'location': 'Location',
            'deadline': 'Deadline',
            'description_file': 'Upload Job Description',
            'link': 'Upload job link'
        }

        widgets = {
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter company name'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Upload company logo'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter job title'}),
            'description': CKEditorWidget(attrs={'class': 'form-control', 'placeholder': 'Enter job description'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter job location'}),
            'deadline': forms.DateInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter application deadline',
                'type': 'date',  # This is HTML5 input type for dates
            }, format='%Y-%m-%d'),
            'description_file': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Upload job description'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Upload job link'}),
        }

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        self.fields['deadline'].input_formats = ['%Y-%m-%d']  # Specify the accepted input formats


class ScholarshipForm(forms.ModelForm):
    class Meta:
        model = Scholarship
        fields = ['image','title','deadline','link']

        labels= {
          'image':'Logo',
          'title':'Title',
          'deadline':'Deadline',
          'link':'Link',  
        }
       
        widgets ={
             'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'upload image'}),
             'title' :  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
             'deadline': forms.DateInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter application deadline',
                'type': 'date',  # This is HTML5 input type for dates
            }, format='%Y-%m-%d'),
             'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Upload scholarship  link'}),
         }
        
    def __init__(self, *args, **kwargs):
        super(ScholarshipForm, self).__init__(*args, **kwargs)
        self.fields['deadline'].input_formats = ['%Y-%m-%d']  # Specify the accepted input formats
