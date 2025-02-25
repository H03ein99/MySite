from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.
def home(request):
    posts = Post.objects.filter(status=1)
    popular_posts = Post.objects.all().filter(status=1).order_by('-counted_view')
    context = {
        'posts' : posts,
        'popular_posts' :popular_posts,
    }
    return render(request, 'blog/blog-home.html', context)

def single(request, id):
    post = get_object_or_404(Post, id=id, status=1)
    popular_posts = Post.objects.all().filter(status=1).order_by('-counted_view')
    context = {
        'post' : post,
        'popular_posts' :popular_posts,
    }
    if post is not None:
        post.counted_view += 1
        post.save()
    return render(request, 'blog/blog-single.html', context)    

# def test(request, id):
#     post = Post.objects.filter(id=id, status=1)[0]
#     context = {'post': post} 
#     return render(request, 'test.html', context)