from django.db import models
from django.conf import settings
# Create your models here.

class Category(models.Model):
    name = models.CharField( max_length=250)

    class Meta:
        verbose_name_plural = ('Categories')

    def __str__(self):
        return self.name
    



class Post(models.Model):
        author =models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            default = -1
        )
        image = models.ImageField(upload_to=settings.MEDIA_ROOT)
        title = models.CharField(max_length=100)
        content = models.TextField()
        category = models.ManyToManyField(Category)
        # tag
        counted_view = models.PositiveIntegerField(default=0)
        status = models.BooleanField(default=False)
        published_date = models.DateTimeField(null=True)
        created_date = models.DateTimeField(auto_now_add=True)
        updated_date = models.DateTimeField(auto_now=True)
        class Meta:
            ordering = ["-created_date"]
        def __str__(self):
            return f"{self.author} - {self.title} - {self.created_date}"


