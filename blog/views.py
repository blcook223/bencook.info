"""
Views for blog app
"""
from django.shortcuts import render, get_object_or_404

from .models import Post, Tag


def blog_home(request):
    """
    Blog homepage with recent posts
    """
    return render(
        request,
        'blog/blog_home.html',
        {
            'current_view': 'blog',
            'tags': Tag.objects.all(),
            'posts': Post.objects.order_by('date')[:5],
        }
    )


def tag(request, slug):
    """
    Index of posts organized by tag
    """
    return render(
        request,
        'blog/tags.html',
        {
            'current_view': 'blog',
            'tag': get_object_or_404(Tag, slug=slug),
            'posts': Post.objects.filter(tags__slug=slug),
        }
    )


def post(request, slug):
    """
    A blog post, identified by title
    """
    return render(
        request,
        'blog/post.html',
        {
            'current_view': 'blog',
            'post': get_object_or_404(Post, slug=slug),
        }
    )
