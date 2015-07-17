from django.db import models


class Tag(models.Model):
    """
    A subject-matter tag for blog posts
    """
    short_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        short_name = name.replace(' ', '-')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Post(models.Model):
    """
    A blog post
    """
    pass
