"""
Views for core app
"""
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError

from bencook_info.settings import ADMIN_EMAILS

from .models import ContactForm


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
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ADMIN_EMAILS)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thank_you')
    else:
        return render(request, 'core/contact.html', {
            'form': ContactForm()
        })

    return render(request, 'core/contact.html', {
        'form': ContactForm()
    })


def thank_you(request):
    """
    Simple thank you for contact page
    """
    return render(request, 'core/thank_you.html')
