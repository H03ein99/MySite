from django import template
from blog.models import Post
from django.utils import timezone


register = template.Library()

@register.inclusion_tag("blog/popularposts.html")
def popularposts():
    posts = Post.objects.filter(status=1).order_by('-counted_view')[:3]
    
    return {
        'posts': posts
        
    }
