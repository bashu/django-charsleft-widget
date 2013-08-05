# -*- coding: utf-8 -*-

from django import forms
from django.utils.encoding import force_unicode
from django.template.loader import render_to_string

__all__ = ['CharsLeftArea']


class MediaMixin(object):

    class Media:
        css = {
            'screen': (
                'charsleft_widget/css/charsleft.min.css',
                )}
        js = ('charsleft_widget/js/charsleft.min.js',)


class CharsLeftArea(forms.Textarea, MediaMixin):
    template_name = 'charsleft_widget/textarea_widget.html'

    def render(self, name, value, attrs=None):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)

        maxlength = final_attrs.get('maxlength', False)
        if not maxlength:
            return super(CharsLeftArea, self).render(name, value, attrs)

        return render_to_string(self.template_name, {
                'id': final_attrs.get('id', None),
                'name': name,
                'widget': super(CharsLeftArea, self).render(name, value, attrs),
                'maxlength': force_unicode(int(maxlength)),
                'current': force_unicode(int(maxlength) - len(value)),
                })
