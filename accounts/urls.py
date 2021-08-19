from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.AccountsSignupView.as_view(), name="signup"),
    path("login/", views.AccountsLoginView.as_view(), name='login'),
    path("logout/", views.AccountsLogoutView.as_view(), name='logout'),
]

# URL's to be implemented
'''
path("password_change/", views.PasswordChangeView.as_view(), name='password_change'),
path("password_change/done/", views.PasswordChangeDoneView.as_view(), name='password_change_done'),
path("password_reset/", views.PasswordResetView.as_view(), name='password_reset'),
path("password_reset/done/", views.PasswordResetDoneView.as_view(), name='password_reset_done'),
path("reset/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
path("reset/done/", views.PasswordResetDoneView.as_view(), name='password_reset_complete'),
'''