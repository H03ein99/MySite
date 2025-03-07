from blog import views
from django.urls import path
app_name = 'blog'
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('single/<int:id>', views.single, name='blog-single'),
    path('category/<str:cat_name>', views.home, name='blog-category'),
    path('tag/<str:tag_name>', views.home, name='blog-tag'),
    path('author/<str:author>', views.home, name='blog-author'),
    path('search/', views.search, name='blog-search'),
    # path('test-<int:id>/', views.test, name='blog-test'),
]
