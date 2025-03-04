from django.urls import path
from accounts.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', login_view, name="login"), # login
    path('logout/', logout_view, name="logout"), #logout
    path('signup/', signup_view, name="signup"), #signup
    # reset and forget password
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"), # password reset
    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"), # password reset
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete") # password reset complete
]