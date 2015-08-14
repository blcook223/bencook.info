"""
Views for personal app
"""

from django.shortcuts import render

from .models import (
    Project,
    OpenSourceContribution,
    Job,
    Skill,
    Testimonial,
    Event,
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
            'events': Event.objects.order_by('order_date'),
            'jobs': Job.objects.order_by('-start_date'),
            'languages': Skill.objects.filter(
                category__exact=Skill.LANGUAGE
            ).order_by('-level'),
            'technical_skills': Skill.objects.filter(
                category__exact=Skill.TECHNICAL
            ).order_by('-level'),
            'testimonies': Testimonial.objects.all(),
        }
    )
