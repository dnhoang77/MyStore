"""MyStore URL Configuration

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
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')), 
    path('', include('store.urls')),
    path('khach-hang/', include('khachhang.urls')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('storereport/', include('storereport.urls', namespace='storereport')),
    path('analysis/', include('analysis.urls', namespace='analysis')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]+static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)