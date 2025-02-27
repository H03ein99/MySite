from django import template
from blog.models import Post, Category
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


@register.inclusion_tag("blog/blog-cats.html")
def blogcats():
    posts = Post.objects.filter(status=1, published_date__lte=today)
    categories = Category.objects.all()
    cat_counts = {}
    for name in categories:
        count =posts.filter(category = name).count()
        if count>0:
            cat_counts[name] = count
    cats = {k: v for k, v in sorted(cat_counts.items(), key=lambda item: item[1], reverse=True)}    
    return {
        
        'categories': cats,
    }

