from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields =['Name','Email','message']

        labels ={
            'Name': 'Name',
            'Email': 'Email',
            'message': 'message'
        }

        widgets ={
           'Name':forms.TextInput(attrs={'class': 'Form-control','placeholder': 'Enter your name'}),
           'Email': forms.EmailInput(attrs={'class': 'Form-control','placeholder': 'Enter your Email'}),
           'message':forms.Textarea(attrs={'class': 'Form-control','placeholder': 'Enter your Messages here....'})
       }