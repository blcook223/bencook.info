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


def date_cmp(item1, item2):
    """
    Compare items for ordering purposes
    """
    if item1.end_date is None and item2.end_date is None:
        if item1.start_date < item2.start_date:
            return 1
        if item2.start_date < item1.start_date:
            return -1
        return 0
    if item1.end_date is None:
        return -1
    if item2.end_date is None:
        return 1
    if item1.end_date < item2.end_date:
        return 1
    if item2.end_date < item1.end_date:
        return -1
    if item1.start_date < item2.start_date:
        return 1
    if item2.start_date < item1.start_date:
        return -1
    return 0


def start_end_key(custom_cmp):
    """
    Compare models with start and end dates.
    """
    class K(object):
        """
        Define comparison operators.
        http://code.activestate.com/recipes/576653-convert-a-cmp-function-to-a-key-function/
        """
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return custom_cmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return custom_cmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return custom_cmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return custom_cmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return custom_cmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return custom_cmp(self.obj, other.obj) != 0
    return K


def portfolio(request):
    """
    Selected software development projects and contributions
    """
    return render(
        request,
        'personal/portfolio.html',
        {
            'current_view': 'portfolio',
            'projects': Project.objects.all(),
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
            'jobs': sorted(Job.objects.all(), key=start_end_key(date_cmp)),
            'languages': Skill.objects.filter(
                category__exact=Skill.LANGUAGE
            ).order_by('-level'),
            'technical_skills': Skill.objects.filter(
                category__exact=Skill.TECHNICAL
            ).order_by('-level'),
            'development_tools': Skill.objects.filter(
                category__exact=Skill.DEV_TOOL
            ).order_by('-level')
            'databases': Skill.objects.filter(
                category__exact=Skill.DATABASE
            ).order_by('-level')
            'testimonies': Testimonial.objects.all(),
        }
    )
