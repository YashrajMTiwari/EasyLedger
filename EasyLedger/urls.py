"""
URL configuration for EasyLedger project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from app import views

urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls),

    # App URLs
    path('app/', include('app.urls')),  # Include the app's urls.py for app-specific routes

    # Redirect to dashboard from the root URL
    path('', lambda request: redirect('dashboard' if request.user.is_authenticated else 'home')),  # Redirect to the dashboard on accessing the root URL

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]

