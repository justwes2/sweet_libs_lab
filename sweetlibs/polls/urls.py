# This is where you will map the view you just defined to a url.
from django.conf.urls import url
# This line pulls url paths from the root url file. More on this next
from . import views
# This is where the views are called from this file, rather than the parent file.
app_name = 'polls'
urlpatterns = [
    # ex /polls/
    url(r'^$', views.index, name='index'),
    # ex /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$',views.detail, name='detail'),
    # ex /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
# This is where the routes are defined.
