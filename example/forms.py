# forms.py
from django import forms

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    C_User = forms.CharField(max_length=20)  # Add C_User field here
