# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode
from django.template.loader import render_to_string
from django.contrib.staticfiles.storage import staticfiles_storage


class MediaMixin(object):

    class Media:
        css = {
            'screen': (
                staticfiles_storage.url(
                    'charsleft_widget/css/charsleft.min.css',
                    ),
                )}
        js = (staticfiles_storage.url('charsleft_widget/js/charsleft.min.js'),)


class CharsLeftArea(forms.Textarea, MediaMixin):

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''

        final_attrs = self.build_attrs(attrs, name=name)

        maxlength = final_attrs.get('maxlength', False)
        if maxlength is False:  # fallback to default widget
            return super(CharsLeftArea, self).render(name, value, attrs)

        if getattr(settings, 'USE_JINJA', False):
            template_name = 'charsleft_widget/textarea.jinja'
        else:
            template_name = 'charsleft_widget/textarea.html'

        output = super(CharsLeftArea, self).render(name, value, attrs)
        return mark_safe(render_to_string(template_name, {
            'name': name,
            'widget': output,
            'maxlength': force_unicode(int(maxlength)),
            'current': force_unicode(int(maxlength) - len(value)),
        }))
