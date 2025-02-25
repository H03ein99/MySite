from django.contrib import admin
from blog.models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ['author', 'title', 'counted_view', 'created_date', 'published_date','id' ]

admin.site.register(Post, PostAdmin)
 