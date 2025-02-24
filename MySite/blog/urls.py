from blog import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('<int:id>', views.single, name='blog-single'),
]
