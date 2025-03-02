from django import forms
from website.models import Contact, Newsletter
from captcha.fields import CaptchaField
class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = "__all__"
    captcha = CaptchaField()    

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = "__all__"

