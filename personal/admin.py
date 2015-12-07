"""
Administrative interface for personal app
"""

from django.contrib import admin

from .models import (
    Skill,
    Image,
    Event,
    Technology,
    Testimonial,
    Job,
    Project,
    Link,
    OpenSourceContribution,
)


class LinkAdmin(admin.ModelAdmin):
    """
    Administrative interface for Link model
    """
    fields = ['href', 'text', 'title', 'target']
    list_display = ['title', 'text', 'href']


class ImageAdmin(admin.ModelAdmin):
    """
    Administrative interface for Image model
    """
    fields = ['title', 'alt', 'file_path', 'link', 'credit']
    list_display = ['title', 'alt']


class EventAdmin(admin.ModelAdmin):
    """
    Administrative interface for Event model
    """
    fieldsets = [
        (None, {'fields': ['name', 'title']}),
        ('Dates', {'fields': ['date', 'order_date']}),
        ('Details', {'fields': ['html', 'images']}),
    ]
    list_display = ['name', 'title', 'date']
    filter_horizontal = ['images']


class JobAdmin(admin.ModelAdmin):
    """
    Administrative interface for Job model
    """
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {'fields': ['start_date', 'end_date']}),
        ('Details', {'fields': ['employer', ]}),
    ]
    list_display = ['title', 'employer', 'start_date', 'end_date']


class TechologyAdmin(admin.ModelAdmin):
    """
    Administrative interface for Technology model
    """
    fields = ['name', 'category']
    list_display = ['name', 'category']


class OpenSourceContributionAdmin(admin.ModelAdmin):
    """
    Administrative interface for OpenSourceContribution model
    """
    fields = ['name', 'link']


class ProjectAdmin(admin.ModelAdmin):
    """
    Administrative interface for Project model
    """
    fieldsets = [
        (None, {'fields': ['name', 'priority']}),
        ('Dates', {'fields': ['start_date', 'end_date']}),
        ('Details', {'fields': [
            'contribution',
            'description',
            'technologies',
            'links'
        ]}),
        ('Images', {'fields': ['first_image', 'second_image']})
    ]
    list_display = ['name', 'start_date', 'end_date']
    filter_horizontal = ['technologies', 'links']


class SkillAdmin(admin.ModelAdmin):
    """
    Administrative interface for Skill model
    """
    fields = ['name', 'category', 'level']
    list_display = ['name', 'category', 'level']


class TestimonialAdmin(admin.ModelAdmin):
    """
    Administrative interface for Testimonial model
    """
    fields = ['source', 'quote']
    list_display = ['source', 'teaser']


admin.site.register(Link, LinkAdmin)
admin.site.register(OpenSourceContribution, OpenSourceContributionAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Technology)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Job, JobAdmin)
