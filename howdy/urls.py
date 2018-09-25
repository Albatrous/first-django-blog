# howdy/urls.py
from django.conf.urls import url
from django.urls import path
from howdy import views


urlpatterns = [
    #url(r'^$', views.HomePageView.as_view()),
	#url(r'^about/$', views.AboutPageView.as_view())
	path('',views.post_list, name='post_list'),
]