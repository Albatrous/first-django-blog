# howdy/urls.py
from django.conf.urls import url
from django.urls import path
from howdy import views


urlpatterns = [
    #url(r'^$', views.HomePageView.as_view()),
	#url(r'^about/$', views.AboutPageView.as_view())
	path('',views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/new/', views.post_new, name='post_new'),
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
	url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
	url(r'^/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]