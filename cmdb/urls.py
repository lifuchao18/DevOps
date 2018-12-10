"""cmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from web.views import userLogin, userLogout, Index, OsView, delete_osinfo, OsCreat, OsUpdate

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', userLogin, name='login'),
    url(r'^index/', Index, name='index'),
    url(r'^logout/', userLogout, name='logout'),
    url(r'^osview/$', OsView, name='osview'),
    url(r'^osview/delete/(?P<_id>\d+)/$', delete_osinfo, name='delete_osinfo'),
    url(r'^osview/osupdate/(?P<_id>\d+)/$', OsUpdate, name='osupdate'),
    url(r'^oscreat/$', OsCreat, name='oscreat'),
    url(r'^', userLogin)
]
