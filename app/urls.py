from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('profile/<slug:user>/', views.profile, name="profile"),
    path('login-request/', views.login_request, name="login_request"),
    path('settings/', views.settings, name="settings"),
    path('delete-account/', views.delete_account, name="delete_account"),
    path('account-deleted/', views.account_deleted, name="account_deleted"),
]
