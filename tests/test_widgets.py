from django import forms
from django.conf import settings
from django.template.loader import get_template
from django.test import TestCase

from charsleft_widget.widgets import CharsLeftArea


class CharsLeftAreaDjangoTest(TestCase):
    def setUp(self):
        self.old_USE_JINJA = getattr(settings, "USE_JINJA", False)
        settings.USE_JINJA = False

        self.field = forms.CharField(required=False, widget=CharsLeftArea)

    def tearDown(self):
        settings.USE_JINJA = self.old_USE_JINJA

    def test_render(self):
        response = self.field.widget.render(
            "value",
            "test",
            {"id": "id_field", "maxlength": 512},
        )
        assert all(s in response for s in ("charsleft", "508"))


class CharsLeftAreaJinjaTest(TestCase):
    def setUp(self):
        self.old_USE_JINJA = getattr(settings, "USE_JINJA", False)
        settings.USE_JINJA = True

        self.field = forms.CharField(required=False, widget=CharsLeftArea)

    def tearDown(self):
        settings.USE_JINJA = self.old_USE_JINJA

    def test_render(self):
        response = self.field.widget.render(
            "value",
            "test",
            {"id": "id_field", "maxlength": 512},
        )
        assert all(s in response for s in ("charsleft", "508"))

    def test_jinja2_backend(self):
        # charsleft_widget/textarea.jinja lives under jinja2/, the app-dirs
        # convention Django's Jinja2 backend uses, so it must be served by
        # a genuine jinja2.Environment rather than falling through to
        # DjangoTemplates just because both accept the same {{ var }} syntax.
        template = get_template("charsleft_widget/textarea.jinja")
        assert template.backend.env.__class__.__module__.startswith("jinja2")


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
