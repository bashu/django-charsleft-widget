from django import forms
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.template.loader import render_to_string
from django.utils.encoding import force_str
from django.utils.safestring import mark_safe


class MediaMixin:
    class Media:  # pylint: disable=C1001
        css = {
            "screen": (
                staticfiles_storage.url(
                    "charsleft_widget/css/charsleft.min.css",
                ),
            )
        }
        js = (staticfiles_storage.url("charsleft_widget/js/charsleft.min.js"),)


class CharsLeftArea(forms.Textarea, MediaMixin):
    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = ""

        final_attrs = self.build_attrs(self.attrs, attrs)

        maxlength = final_attrs.get("maxlength", False)
        if maxlength is False:  # fallback to default widget
            return super().render(name, value, attrs, renderer)

        if getattr(settings, "USE_JINJA", False):
            template_name = "charsleft_widget/textarea.jinja"
        else:
            template_name = "charsleft_widget/textarea.html"

        output = super().render(name, value, attrs, renderer)
        return mark_safe(
            render_to_string(
                template_name,
                {
                    "name": name,
                    "widget": output,
                    "maxlength": force_str(int(maxlength)),
                    "current": force_str(int(maxlength) - len(value)),
                },
            )
        )
