from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("signup/", views.AccountsSignupView.as_view(), name="signup"),
    path("login/", views.AccountsLoginView.as_view(), name='login'),
    path("logout/", views.AccountsLogoutView.as_view(), name='logout'),
]

# URL's to be implemented
'''
path("password_change/", auth_views.PasswordChangeView.as_view(), name='password_change'),
path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
path("password_reset/", auth_views.PasswordResetView.as_view(), name='password_reset'),
path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
path("reset/done/", auth_views.PasswordResetDoneView.as_view(), name='password_reset_complete'),
'''