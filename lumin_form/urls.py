"""lumin_form URL Configuration

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
from hello import views
from django.urls import path
app_name = "hello"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('jisuan/', views.calculate),
    path('counter/', views.jisuan),
    path('getdata/', views.show),
    path('insert/', views.insert, name='register'),
    path('index/', views.index, name='index'),
    path('edit/', views.edit),
    path('delete_user/(?P<UserInfo_id>[0-9]+)/$',views.delete_user,name='delete_user'),
    path('upload/', views.upload),
]