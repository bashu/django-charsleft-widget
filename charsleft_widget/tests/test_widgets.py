# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.test import TestCase

from ..widgets import CharsLeftArea


class CharsLeftAreaTest(TestCase):

    def test_default(self):
        self.field = forms.CharField(required=False, widget=CharsLeftArea)

        response = self.field.widget.render('value', None, {'id': 'id_field', 'maxlength': 512})
        self.assertTrue('charsleft' in response and "count" in response)

    def test_fallback(self):
        self.field = forms.CharField(required=False, widget=CharsLeftArea)

        response = self.field.widget.render('value', None, {'id': 'id_field'})
        self.assertFalse('charsleft' in response and "count" in response)
