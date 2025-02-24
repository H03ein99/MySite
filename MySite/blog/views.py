from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blog/blog-home.html')

def single(request):
    return render(request, 'blog/blog-single.html')    