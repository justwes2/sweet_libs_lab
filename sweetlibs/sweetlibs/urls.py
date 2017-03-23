"""sweetlibs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# Here you will define the app paths within the project
from django.conf.urls import include, url
# make sure to add include here, it does not do so automatically
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    # This line will be added to address any /polls requests
    url(r'^admin/', admin.site.urls),
]
