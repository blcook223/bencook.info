"""
Forms for core app
"""
from django import forms


class ContactForm(forms.Form):
    """
    A simple contact form
    """
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    subject = forms.CharField(initial='bencook.info : Contact Form Submission')
    message = forms.CharField(widget=forms.Textarea)
