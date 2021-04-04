"""charitydonation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from charity.views import (
                        LandingPage,
                        Register,
                        AddDonation,
                        FormConfirmation,
                        UserProfile,
                        CustomLogin,
                        UserSettings,
                        )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(
                    template_name='password_change_done.html'), name='change-password-done'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', CustomLogin.as_view(), name='login'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
                    template_name='password_change.html'), name='change-password'),
    path('', LandingPage.as_view(), name='landing-page'),
    path('register/', Register.as_view(), name='register'),
    path('add-donation/', AddDonation.as_view(), name='add-donation'),
    path('confirmation/', FormConfirmation.as_view(), name='form-confirmation'),
    path('profile/', UserProfile.as_view(), name='profile'),
    path('settings/<int:pk>/', UserSettings.as_view(), name='settings'),
]
