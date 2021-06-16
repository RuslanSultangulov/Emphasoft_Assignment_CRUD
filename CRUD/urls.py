"""CRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from app.views import ApiTokenAuth, UsersView, UsersViewById


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', ApiTokenAuth.as_view(), name='api_token_auth'),
    path('api/users/', UsersView.as_view(), name='users_view'),
    path('api/users/<int:pk>', UsersViewById.as_view(),
         name='user_view_by_id'),
]
