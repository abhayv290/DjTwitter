"""
URL configuration for djX project.

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
from django.urls import path,include,re_path
from django.shortcuts import render
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.auth.urls import views as auth_views
from . import settings

def  homeView(req):
    return render(req,'index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
 
re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    path('',homeView,name='home'),
    path('tweet/',  include('tweet.urls'),name='tweet'),
    path('accounts/',include('django.contrib.auth.urls'),name='accounts')
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)