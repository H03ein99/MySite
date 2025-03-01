from django.shortcuts import render
from website.forms import ContactForm, NewsletterForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'website/index.html' )

def about(request):
    return render(request, 'website/about.html') 

def contact(request):
    if request.method == 'POST':
        form = ContactForm(data = request.POST)
        if form.is_valid():
            contact = form.save(commit = False)
            contact.name = 'unknown'
            contact.save()
            messages.add_message(request, messages.SUCCESS, 'Your message has been sent successfuly!')
        else:
            messages.add_messafe(request, messages.ERROR, 'Some error occurred during submiting your message. please try again.')    
                
          
    return render(request, 'website/contact.html')       

def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(data = request.POST)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Your email has been added successfuly!')
        return HttpResponseRedirect("/")
    else:
        messages.add_message(request, messages.ERROR, 'We had a problem while adding your email address. please try again.')           
        return HttpResponseRedirect("/")