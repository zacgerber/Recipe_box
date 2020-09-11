"""recipes URL Configuration

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
from django.urls import path

from homepage import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('post/<int:post_id>/', views.post_detail),
    path('author/<int:post_id>/', views.author_detail),
    path('edit_recipe/<int:recipe_id>/', views.edit_recipe_view),
    path('add_favorites/<int:recipe_id>/', views.add_favorites_view),
    path('addrecipe/', views.recipe_form_view, name="addrecipe"),
    path('addauthor/', views.author_form_view, name="addauthor"),
    path('login/', views.login_view, name="loginview"),
    path('logout/', views.logout_view, name="logoutview"),
    path('admin/', admin.site.urls),
]
