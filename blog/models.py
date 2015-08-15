from django.db import models
from django.core.urlresolvers import reverse


class Tag(models.Model):
    """
    A subject-matter tag for blog posts
    """
    slug = models.CharField(max_length=200, unique=True)
    name = models.SlugField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(' ', '-')[:50]

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

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(' ', '-')[:50]

    def get_absolute_url(self):
        return reverse('post', args=(self.slug,))

    def teaser(self):
        return self.body[:100]

    class Meta:
        ordering = ('title', 'date', 'body')
