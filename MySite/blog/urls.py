from blog import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('single/<int:id>', views.single, name='blog-single'),
    # path('test-<int:id>/', views.test, name='blog-test'),
]
