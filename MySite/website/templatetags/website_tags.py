from django import template
from blog.models import Post, Category
from django.utils import timezone

today = timezone.now()
register = template.Library()

@register.inclusion_tag("website/blog-recent.html")
def blog_recent_posts():
    posts = Post.objects.filter(status=1, published_date__lte=today).order_by('-published_date')[:6]
     
    return {
        'posts': posts,
        
    }
