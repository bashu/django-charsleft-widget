# -*- coding: utf-8 -*-

from django.conf.urls import *

from .views import TestView

urlpatterns = patterns('',
    url(r'^$', TestView.as_view(template_name='homepage.html')),
)
