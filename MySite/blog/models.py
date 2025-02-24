from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
        author =models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            default = -1
        )
        image = models.ImageField(upload_to=settings.MEDIA_ROOT)
        title = models.CharField(max_length=100)
        content = models.TextField()
        # category 
        # tag
        counted_view = models.PositiveIntegerField(default=0)
        status = models.BooleanField(default=False)
        published_date = models.DateField(null=True)
        created_date = models.DateField(auto_now_add=True)
        updated_date = models.DateField(auto_now=True)
        class Meta:
            ordering = ["-created_date"]
        def __str__(self):
            return f"{self.author} - {self.title} - {self.created_date}"
    
