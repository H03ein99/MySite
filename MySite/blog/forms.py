from django import forms
from blog.models import Comment
from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = "__all__"
    # captcha = CaptchaField()
    def clean_post(self):
        post = self.cleaned_data.get('post')
        if not post:
            raise forms.ValidationError("This Field is Required")
        return post