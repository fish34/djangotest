from django.conf.urls import url
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^test/$', RedirectView.as_view(url=r'https://google.com')), #google
]