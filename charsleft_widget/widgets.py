# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.contrib.staticfiles.storage import staticfiles_storage

try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text


class MediaMixin(object):

    class Media:  # pylint: disable=C1001
        css = {
            'screen': (
                staticfiles_storage.url(
                    'charsleft_widget/css/charsleft.min.css',
                    ),
                )}
        js = (staticfiles_storage.url('charsleft_widget/js/charsleft.min.js'),)


class CharsLeftArea(forms.Textarea, MediaMixin):

    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = ''

        final_attrs = self.build_attrs(self.attrs, attrs)

        maxlength = final_attrs.get('maxlength', False)
        if maxlength is False:  # fallback to default widget
            return super(CharsLeftArea, self).render(name, value, attrs, renderer)

        if getattr(settings, 'USE_JINJA', False):
            template_name = 'charsleft_widget/textarea.jinja'
        else:
            template_name = 'charsleft_widget/textarea.html'

        output = super(CharsLeftArea, self).render(name, value, attrs, renderer)
        return mark_safe(render_to_string(template_name, {
            'name': name,
            'widget': output,
            'maxlength': force_text(int(maxlength)),
            'current': force_text(int(maxlength) - len(value)),
        }))
