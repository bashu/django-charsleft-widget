# -*- coding: utf-8 -*-

import django

from django import forms
from django.views.generic import FormView

if django.VERSION < (1,7):
    from charsleft_widget.fields import CharField
else:
    from django.forms.fields import CharField

from charsleft_widget import CharsLeftArea


class TestForm(forms.Form):

    field = CharField(max_length=128, widget=CharsLeftArea)

               
class TestView(FormView):
    form_class = TestForm
