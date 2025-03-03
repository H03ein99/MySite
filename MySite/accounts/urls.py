from django.urls import path
from accounts import views
app_name = "accounts"

urlpatterns = [
    path('login/', login_view, name="login"), # login
    # path('logout/', logout_view, name="logout"),
    path('signup/', signup_view, name="signup"), #signup
]