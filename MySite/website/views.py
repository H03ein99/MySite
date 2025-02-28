from django.shortcuts import render
from blog.models import Post, Category
from django.utils import timezone
# Create your views here.
today = timezone.now()
def index(request):
    posts = Post.objects.filter(status=1, published_date__lte=today).order_by('-published_date')[:6]
    context = {
        'posts': posts
    }
    return render(request, 'website/index.html', context)

def about(request):
    return render(request, 'website/about.html') 

def contact(request):
    return render(request, 'website/contact.html')       