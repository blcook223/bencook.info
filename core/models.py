"""
Models for core app
"""
from django import forms


class ContactForm(forms.Form):
    """
    A simple contact form
    """
    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea())
