from django import forms
from django.test import TestCase

from charsleft_widget.widgets import CharsLeftArea


class CharsLeftAreaDjangoTest(TestCase):
    def setUp(self):
        self.field = forms.CharField(required=False, widget=CharsLeftArea)

    def test_render(self):
        response = self.field.widget.render(
            "value",
            "test",
            {"id": "id_field", "maxlength": 512},
        )
        assert all(s in response for s in ("charsleft", "508"))


class CharsLeftAreaOverflowTest(TestCase):
    def setUp(self):
        self.field = forms.CharField(required=False, widget=CharsLeftArea)

    def test_value_already_over_maxlength(self):
        response = self.field.widget.render(
            "value",
            "x" * 20,
            {"id": "id_field", "maxlength": 10},
        )
        assert "-10" in response


class CharsLeftAreaFallbackTest(TestCase):
    def setUp(self):
        self.field = forms.CharField(required=False, widget=CharsLeftArea)

    def test_fallback(self):
        response = self.field.widget.render("value", None, {"id": "id_field"})
        assert not ("charsleft" in response and "count" in response)
