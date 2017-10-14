from django.conf.urls import url,patterns
from . import views
# urlpatterns = patterns('booktest.views',(r'^$','index'),)
urlpatterns = [
    url(r'^$',views.index),
    url(r'^get1/$', views.get1),
    url(r'^get2/$', views.get2),
    url(r'^get3/$', views.get3),
    url(r'^post1/$', views.post1),
    url(r'^post2/$', views.post2),
    url(r'^red1/$', views.red1),
    url(r'^cookie_set/$',views.cookie_set),
    url(r'^cookie_get/$',views.cookie_get),
    url(r'^session_test/$',views.session_test),
    url(r'^session_get/$',views.session_get),
    url(r'^session_delete/$',views.session_delete),
    url(r'^json1/$', views.json1),
    url(r'^json2/$', views.json2),
    url(r'^delete(\d+)/', views.delete),
    url(r'^create/$', views.create),
    url(r'^(?P<id1>\d+)/(?P<id2>\d+)/(?P<id3>\d+)/$', views.show1),
]