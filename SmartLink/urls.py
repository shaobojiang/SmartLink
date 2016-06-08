from django.conf.urls import patterns, include, url
from django.contrib import admin
from MyHttpServer import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SmartLink.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', views.register, name='register'),
    url(r'^users/$', views.users, name='users'),
    url(r'^login/$', views.login, name='login'),
    url(r'^send_message/$', views.sendMessage, name='sendMessage'),
    
)
