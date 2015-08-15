from django.shortcuts import render


def blog_home(request):
    """
    Blog homepage with recent posts
    """
    return render(
        request,
        'blog/blog_home.html',
        {
            'current_view': 'blog'
        }
    )


def tags(request, tag=None):
    """
    Index of posts organized by tag
    """
    return render(
        request,
        'blog/tags.html',
        {
            'current_view': 'blog'
        }
    )


def post(request, short_title):
    """
    A blog post, identified by title
    """
    return render(
        request,
        'blog/post.html',
        {
            'current_view': 'blog'
        }
    )
