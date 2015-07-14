from django.shortcuts import render

from .models import Project, OpenSourceContribution

def index(request):
    """
    Homepage of personal app and website
    """
    return render(
        request,
        'personal/index.html',
        {
            'current_view': 'index'
        }
    )


def portfolio(request):
    """
    Selected software development projects and contributions
    """
    return render(
        request,
        'personal/portfolio.html',
        {
            'current_view': 'portfolio',
            'projects': Project.objects.order_by('-start_date'),
            'open_source_contribs': OpenSourceContribution.objects.all(),
        }
    )


def about(request):
    """
    Biographical information
    """
    pass


def contact(request):
    """
    A contact form
    """
    pass


def resume(request):
    """
    Professional experience, education, and skills
    """
    pass
