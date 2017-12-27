#-*- coding: utf-8 -*-
'''
    Author: smallmi
    Blog: http://www.smallmi.com
'''
from __future__ import unicode_literals

from django.conf.urls import url
from dashboard import views 

urlpatterns = [

    url(r'^$', views.index, name='dashboard_index'),
    url(r'^index$', views.index_data,name='index_data'),
    url(r'^select$', views.select_data,name='select_data'),
    # url(r'^getAllUser/$', views.getAllUser, name='getAllUser'),
    # url(r'^getAllHost/$', views.getAllHost, name='getAllHost'),
    # url(r'^getAllPlatform/$', views.getAllPlatform, name='getAllPlatform'),
    # url(r'^getAllAppProject/$', views.getAllAppProject, name='getAllAppProject'),

]
