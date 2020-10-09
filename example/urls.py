# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import TestView

urlpatterns = [
    url(r"^$", TestView.as_view(template_name="homepage.html")),
]
