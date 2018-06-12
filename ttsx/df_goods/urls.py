#-*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
from views import *


urlpatterns=[
    url(r'^$',views.index),
    url(r'^list(\d+)_(\d+)_(\d+)/$',views.goodlist),
    url(r'^(\d+)/$', views.detail),
    #自定义全文检索的视图
    # url(r'^search/',MysearchView())
]