# -*- coding: utf-8 -*-

from django import forms


class CharField(forms.CharField):

    def widget_attrs(self, widget):
        attrs = super(CharField, self).widget_attrs(widget)  # NOQA
        if self.max_length is not None:
            # The HTML attribute is maxlength, not max_length.
            attrs.update({'maxlength': str(self.max_length)})
        return attrs

