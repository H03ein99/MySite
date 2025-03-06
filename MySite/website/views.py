from django.shortcuts import render, redirect
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
            messages.success(request, 'Your message has been sent successfuly!')
            return redirect('/contact')
        else:
            messages.error(request, 'Some error occurred during submiting your message. please try again.')   
    else:
        form = ContactForm()
        context = {'form': form}            
          
    return render(request, 'website/contact.html', context)       

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


# coming soon: just activate during maintenance or pre-launch page        
def coming_soon(request):
    return render(request, 'coming_soon.html')