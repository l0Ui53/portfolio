from django import forms
from .models import Contact

class SkillSearchForm(forms.Form):
    skill = forms.CharField(label='Search for skill', max_length=100)

class ContactForm(forms.ModelForm):
    pass