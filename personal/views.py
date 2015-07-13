from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    """
    Homepage of personal app and website
    """
    return render(request, 'personal/index.html')


def portfolio(request):
    """
    Selected software development projects and contributions
    """
    return HttpResponse('portfolio')


def about(request):
    """
    Biographical information
    """
    return HttpResponse('about')


def contact(request):
    """
    A contact form
    """
    return HttpResponse('contact')


def resume(request):
    """
    Professional experience, education, and skills
    """
    return HttpResponse('resume')
