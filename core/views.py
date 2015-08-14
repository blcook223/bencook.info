"""
Views for core app
"""
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail

from bencook_info.settings import ADMIN_EMAILS

from .forms import ContactForm


def index(request):
    """
    Homepage of personal app and website
    """
    return render(
        request,
        'core/index.html',
        {
            'current_view': 'index',
        }
    )


def contact(request):
    """
    Simple contact page for website
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            send_mail(
                subject,
                ' '.join(['From:', name, 'Message:', message]),
                from_email,
                ADMIN_EMAILS
            )
            return HttpResponseRedirect('/contact/thank_you')
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {
        'form': form
    })


def thank_you(request):
    """
    Simple thank you for contact page
    """
    return render(request, 'core/thank_you.html')
