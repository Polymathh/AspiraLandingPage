from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['first_name', 'second_name', 'phone', 'email', 'level_of_language']