# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.test import TestCase

from ..widgets import CharsLeftArea


class CharsLeftAreaTest(TestCase):

    def test_empty(self):
        self.field = forms.CharField(required=False, widget=CharsLeftArea)

        response = self.field.widget.render('value', None, {'id': 'id_field', 'maxlength': 512})
        self.assertTrue('charsleft' in response and not "None" in response)
