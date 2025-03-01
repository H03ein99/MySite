from django.shortcuts import render
from website.forms import ContactForm, NewsletterForm
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def index(request):
    return render(request, 'website/index.html' )

def about(request):
    return render(request, 'website/about.html') 

def contact(request):
    if request.method == 'POST':
        form = ContactForm(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
                
          
    return render(request, 'website/contact.html')       

def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(data = request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponse("NOT VALID")            