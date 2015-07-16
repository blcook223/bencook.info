from django.shortcuts import render

from .models import (
    Project,
    OpenSourceContribution,
    Job,
    Skill,
    Testimonial,
    Event,
)


def index(request):
    """
    Homepage of personal app and website
    """
    return render(
        request,
        'personal/index.html',
        {
            'current_view': 'index',
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
    return render(
        request,
        'personal/about.html',
        {
            'current_view': 'about',
            'events': Event.objects.order_by('order_date')
        }
    )


def contact(request):
    """
    A contact form
    """
    pass


def resume(request):
    """
    Professional experience, education, and skills
    """
    return render(
        request,
        'personal/resume.html',
        {
            'current_view': 'resume',
            'jobs': Job.objects.order_by('-start_date'),
            'languages': Skill.objects
                .filter(category__exact=Skill.LANGUAGE)
                .order_by('-level'),
            'technical_skills': Skill.objects
                .filter(category__exact=Skill.TECHNICAL)
                .order_by('-level'),
            'testimonies': Testimonial.objects.all(),
        }
    )
