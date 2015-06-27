from django.db import models


# class Event(models.Model):
#     pass


# class Project(models.Model):
#     pass


class Skill(models.Model):
    """
    Technical or professional skill
    """
    TECHNICAL = 'T'
    PROFESSIONAL = 'P'
    CATEGORY_CHOICES = (
        (TECHNICAL, 'Technical'),
        (PROFESSIONAL, 'Professional'),
    )
    BEGINNER = '1'
    INTERMEDIATE = '2'
    COMPETENT = '3'
    PROFICIENT = '4'
    EXPERT = '5'
    LEVEL_CHOICES = (
        (BEGINNER, 'Beginner (1)'),
        (INTERMEDIATE, 'Intermediate (2)'),
        (COMPETENT, 'Competent (3)'),
        (PROFICIENT, 'Proficient (4)'),
        (EXPERT, 'Expert (5)'),
    )
    category = models.CharField(max_length=1,
                                choices=CATEGORY_CHOICES,
                                default=TECHNICAL)
    level = models.CharField(max_length=1,
                             choices=LEVEL_CHOICES,
                             default=BEGINNER)
    name = models.CharField(max_length=200)


# class Testimonial(models.Model):
#     """
#     Testimony from a customer or coworker
#     """
#     pass


# class Job(models.Model):
#     pass
