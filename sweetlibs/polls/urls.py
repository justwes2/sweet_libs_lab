# This is where you will map the view you just defined to a url. 
from django.conf.urls import url
# This line pulls url paths from the root url file. More on this next
from . import views
# This is where the views are called from this file, rather than the parent file.
urlpatterns = [
    url(r'^$', views.index, name='index')
]
# This is where the routes are defined.
