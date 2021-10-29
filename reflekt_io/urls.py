"""reflekt_io URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from main.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    # Main URL (currently hello world)
    path('', include('main.urls')),
    # URL integration
    path('journal/', include('journal.urls', namespace='journal')),
    path('pojok-curhat/', include('pojok_curhat.urls', namespace='pojok_curhat')),
    path('tembok-harapan/', include('tembok_harapan.urls', namespace='tembok_harapan')),
    path('kutipan-penyemangat/', include('kutipan_penyemangat.urls', namespace='kutipan_penyemangat')),
    path('deteksi-depresi/', include('deteksi_depresi.urls', namespace='deteksi_depresi')),
    path('refleksi/', include('refleksi.urls', namespace='refleksi')),
    path('about-us/', include('about_us.urls', namespace='about_us')),
]
