from django import template
from blog.models import Post
from django.utils import timezone

today = timezone.now()
register = template.Library()

@register.inclusion_tag("blog/blog-popular-posts.html")
def popularposts():
    posts = Post.objects.filter(status=1).order_by('-counted_view')[:3]
    
    return {
        'posts': posts,
        
    }

@register.inclusion_tag("blog/blog-recent-posts.html")
def recentposts():
    posts = Post.objects.filter(status=1, published_date__lte=today).order_by('-published_date')[:3]
    
    return {
        'posts': posts,
        
    }


