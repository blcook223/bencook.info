from django.db import models
from django.utils import timezone


class Link(models.Model):
    """
    A link
    """
    title = models.CharField(max_length=200,
                             null=True,
                             blank=True)
    href = models.CharField('URL',
                            max_length=200,
                            null=True,
                            blank=True)
    text = models.CharField(max_length=200,
                            null=True,
                            blank=True)
    target = models.BooleanField('Open in new tab',
                                 default=False)

    def __str__(self):
        return '{} ({})'.format(self.title, self.href)

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.text()
        super(Link, self).save(*args, **kwargs)

    class Meta:
        ordering = ('text',)


class Image(models.Model):
    """
    An image
    """
    title = models.CharField(max_length=200,
                             null=True,
                             blank=True)
    image_file = models.ImageField(upload_to='uploaded/personal')
    alt = models.CharField('alt text',
                           max_length=500)
    link = models.ForeignKey(Link,
                             null=True,
                             blank=True)
    credit = models.CharField(max_length=200,
                              null=True,
                              blank=True)

    def __str__(self):
        return self.title


class Event(models.Model):
    """
    A biographical event
    """
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    order_date = models.DateField(default=timezone.now,
                                  null=True,
                                  blank=True)
    html = models.TextField('HTML content')
    images = models.ManyToManyField(Image)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('order_date',)


class Technology(models.Model):
    """
    The name of a technology used in a project
    """
    LANGUAGE = 'A'
    FRAMEWORK = 'B'
    DATABASE = 'C'
    EDITOR = 'D'
    OTHER = 'E'
    CATEGORY_CHOICES = (
        (LANGUAGE, 'Language'),
        (FRAMEWORK, 'Framework'),
        (DATABASE, 'Database'),
        (EDITOR, 'Editor'),
        (OTHER, 'Other'),
    )

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=1,
                                choices=CATEGORY_CHOICES,
                                default=LANGUAGE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('category', 'name')
        verbose_name_plural = 'technologies'
        unique_together = (('name', 'category'),)


class OpenSourceContribution(models.Model):
    """
    An open-source project to which a contribution has been
    made
    """
    name = models.CharField(max_length=200)
    link = models.ForeignKey(Link)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'open-source contribution'


class Project(models.Model):
    """
    A project in the portfolio
    """
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now,
                                null=True,
                                blank=True)
    name = models.CharField(max_length=200)
    contribution = models.CharField(max_length=200)
    technologies = models.ManyToManyField(Technology)
    description = models.TextField()
    links = models.ManyToManyField(Link,
                                   blank=True)
    first_image = models.ForeignKey(Image,
                                    related_name='first_project_image',
                                    null=True)
    second_image = models.ForeignKey(Image,
                                     related_name='second_project_image',
                                     null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-end_date', 'start_date')


class Skill(models.Model):
    """
    Technical or professional skill
    """
    TECHNICAL = 'T'
    PROFESSIONAL = 'P'
    LANGUAGE = 'L'
    CATEGORY_CHOICES = (
        (TECHNICAL, 'Technical'),
        (PROFESSIONAL, 'Professional'),
        (LANGUAGE, 'Language')
    )
    BEGINNER = '1'
    INTERMEDIATE = '2'
    COMPETENT = '3'
    PROFICIENT = '4'
    EXPERT = '5'
    LEVEL_CHOICES = (
        (BEGINNER, 'Beginner ({})'.format(BEGINNER)),
        (INTERMEDIATE, 'Intermediate ({})'.format(INTERMEDIATE)),
        (COMPETENT, 'Competent ({})'.format(COMPETENT)),
        (PROFICIENT, 'Proficient ({})'.format(PROFICIENT)),
        (EXPERT, 'Expert ({})'.format(EXPERT)),
    )
    category = models.CharField(max_length=1,
                                choices=CATEGORY_CHOICES,
                                default=LANGUAGE)
    level = models.CharField(max_length=1,
                             choices=LEVEL_CHOICES,
                             default=BEGINNER)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('category', 'level', 'name')


class Testimonial(models.Model):
    """
    Testimony from a customer or coworker
    """
    quote = models.TextField()
    source = models.CharField(max_length=200)

    def teaser(self):
        return self.quote[:50] + '...'

    def __str__(self):
        return self.source


class Job(models.Model):
    """
    A professional position
    """
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now,
                                null=True,
                                blank=True)
    title = models.CharField(max_length=200)
    employer = models.CharField(max_length=200)

    def __str__(self):
        return '{}, {}'.format(self.title, self.employer)

    class Meta:
        ordering = ('-end_date', 'start_date')
