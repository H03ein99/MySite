from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone

# Create your views here.
today = timezone.now().date()
def home(request):
    
    posts = Post.objects.filter(status=1, published_date__lte=today).order_by('-published_date')
    popular_posts = Post.objects.all().filter(status=1).order_by('-counted_view')[:3]
    context = {
        'posts' : posts,
        'popular_posts' :popular_posts,
    }
    return render(request, 'blog/blog-home.html', context)

def single(request, id):
    post = get_object_or_404(Post, id=id, status=1, published_date__lte=today)
    popular_posts = Post.objects.all().filter(status=1).order_by('-counted_view')
    previous = post.previous_post()
    next = post.next_post()
    context = {
        'post' : post,
        'popular_posts' :popular_posts,
        'prev': previous,
        'next': next,
    }
    if post is not None:
        post.counted_view += 1
        post.save()
    return render(request, 'blog/blog-single.html', context)    

# def test(request, id):
#     post = Post.objects.filter(id=id, status=1)[0]
#     context = {'post': post} 
#     return render(request, 'test.html', context)