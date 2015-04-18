# -*- coding: utf-8 -*-

from django import forms
from django.views.generic import FormView

from charsleft_widget import CharsLeftArea


class TestForm(forms.Form):

    field = forms.CharField(max_length=128, widget=CharsLeftArea)

               
class TestView(FormView):
    form_class = TestForm
