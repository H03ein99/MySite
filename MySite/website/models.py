from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField( max_length=255)
    subject = models.CharField( max_length=255)
    email = models.EmailField()
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    
class Newsletter(models.Model):
    email = models.EmailField()    

    def __str__(self):
        return self.email
    