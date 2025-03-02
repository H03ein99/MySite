from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.utils import timezone
from django.urls import reverse

class BlogSitemap(Sitemap):
    today = timezone.now()
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=True, published_date__lte=self.today)

    def lastmod(self, obj):
        return obj.published_date

    def location(self, item):    
        return reverse("blog:blog-single", kwargs = {'id': item.id})