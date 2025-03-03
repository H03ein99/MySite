from django.contrib import admin
from blog.models import Post, Category, Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    
    list_display = ['author', 'title', 'counted_view', 'created_date', 'published_date','id' ]

class CommentAdmin(admin.ModelAdmin):
    date_hierarchi = 'created_date'
    empty_value_display = '---'
    list_filter = ('post', 'approved',)
    list_display = ['post', 'name', 'approved', 'created_date', ]

admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
 