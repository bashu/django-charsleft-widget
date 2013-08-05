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


class CharsLeftAreaDjangoTest(TestCase):

    def setUp(self):
        self.old_USE_JINJA = getattr(settings, 'USE_JINJA', False)
        settings.USE_JINJA = False

    def tearDown(self):
        settings.USE_JINJA = self.old_USE_JINJA

    def test_template(self):
        self.field = forms.CharField(required=False, widget=CharsLeftArea)
        response = self.field.widget.render('value', 'test', {'id': 'id_field', 'maxlength': 512})
        self.assertTrue('charsleft' in response and '508' in response)


class CharsLeftAreaJinjaTest(TestCase):

    def setUp(self):
        self.old_USE_JINJA = getattr(settings, 'USE_JINJA', False)
        settings.USE_JINJA = True

    def tearDown(self):
        settings.USE_JINJA = self.old_USE_JINJA

    def test_template(self):
        self.field = forms.CharField(required=False, widget=CharsLeftArea)
        response = self.field.widget.render('value', 'test', {'id': 'id_field', 'maxlength': 512})
        self.assertTrue('charsleft' in response and '508' in response)
