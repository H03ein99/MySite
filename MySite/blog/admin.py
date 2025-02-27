from django.contrib import admin
from blog.models import Post, Category
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    
    list_display = ['author', 'title', 'counted_view', 'created_date', 'published_date','id' ]

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
 