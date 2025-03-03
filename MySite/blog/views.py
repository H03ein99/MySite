from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
today = timezone.now()
def home(request, **kwargs):
    posts = Post.objects.filter(status=1, published_date__lte=today).order_by('-published_date')
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author') != None:
        posts = posts.filter(author__username=kwargs['author'])  
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tag__name__in=[kwargs['tag_name']])      
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)        
 
    popular_posts = Post.objects.all().filter(status=1).order_by('-counted_view')[:3]
    context = {
        'posts' : posts,
        'popular_posts' :popular_posts,
    }
    return render(request, 'blog/blog-home.html', context)

def single(request, id):
    post = get_object_or_404(Post, id=id, status=1, published_date__lte=today)
    comments = Comment.objects.filter(post= post.id)
    popular_posts = Post.objects.all().filter(status=1).order_by('-counted_view')
    previous = Post.objects.filter(status=1, published_date__lte=today, id__lt=post.id).order_by('-id').first()
    next = Post.objects.filter(status=1, published_date__lte=today, id__gt=post.id).order_by('id').first()
    context = {
        'post' : post,
        'popular_posts' :popular_posts,
        'prev': previous,
        'next': next,
        'comments': comments
    }
    if post is not None:
        post.counted_view += 1
        post.save()
    return render(request, 'blog/blog-single.html', context)    

def search(request):
    posts = Post.objects.filter(status=1, published_date__lte=today)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)        



# def test(request, id):
#     post = Post.objects.filter(id=id, status=1)[0]
#     context = {'post': post} 
#     return render(request, 'test.html', context)