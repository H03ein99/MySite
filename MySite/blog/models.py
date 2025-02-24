from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
        author =models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=model.CASCADE,
        )
        image = models.image_field(upload_to='uploads/% Y/% m/% d/')
        title = models.CharField(max_length=100)
        content = models.TextField()
        # category 
        # tag
        counted_view = models.PositiveIntegerField(default=0)
        status = models.BooleanField(default=False)
        published_date = models.DateField(null=True)
        created_date = models.DateField(auto_now_add=True)
        updated_date = models.DateField(auto_add=True)

    def __str__(self):
        return f"{self.title} - {self.author}"
    
