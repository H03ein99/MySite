from blog import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('single/<int:id>', views.single, name='blog-single'),
    path('category/<str:cat_name>', views.home, name='blog-category'),
    path('author/<str:author>', views.home, name='blog-author'),
    # path('test-<int:id>/', views.test, name='blog-test'),
]
