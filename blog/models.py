from markdown import markdown

from django.db import models
from django.core.urlresolvers import reverse


class Tag(models.Model):
    """
    A subject-matter tag for blog posts
    """
    slug = models.CharField(max_length=200, unique=True)
    name = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag', args=(self.slug,))

    class Meta:
        ordering = ('name',)


class Post(models.Model):
    """
    A blog post
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', args=(self.slug,))

    def teaser(self):
        return ' '.join([self.body[:100], '...'])

    def body_html( self ):
        return markdown(self.body)

    class Meta:
        ordering = ('title', 'date', 'body')
