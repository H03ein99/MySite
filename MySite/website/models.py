from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField( max_length=255)
    subject = models.CharField( max_length=255, blank=True, null=True)
    email = models.EmailField(null = True, blank=True)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    # if I want to always save name as unknown this method will work too.
    # def save(self, *args, **kwargs):
    #     self.name = "unknown"
    #     super().save(*args, **kwargs)
    
    
class Newsletter(models.Model):
    email = models.EmailField()    

    def __str__(self):
        return self.email
    