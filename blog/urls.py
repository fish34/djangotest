from django.urls import re_path
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    re_path(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='blog/registration/login.html'), name='login'),
    re_path(r'^accounts/logout/$', auth_views.LogoutView.as_view(), name='logout'),
    #re_path(r'',TemplateView.as_view(template_name="main.html")),
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'^test/$', views.redirect_view), #google
    re_path(r'^post/new/$', views.post_new, name='post_new'),
    re_path(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    re_path(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
    re_path(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    re_path(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    re_path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    re_path(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    re_path(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]
