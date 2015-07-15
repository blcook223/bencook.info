from django import template

from ..models import Skill


register = template.Library()


@register.filter(name='skill_level')
def skill_level(value):
    if value == Skill.BEGINNER:
        return 'beginner'
    elif value == Skill.INTERMEDIATE:
        return 'intermediate'
    elif value == Skill.COMPETENT:
        return 'competent'
    elif value == Skill.PROFICIENT:
        return 'proficient'
    elif value == Skill.EXPERT:
        return 'expert'
