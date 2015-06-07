django-charsleft-widget
===

django-charsleft-widget is a custom widget that limits the number of characters that can be entered in a textarea  field. The widget can also report the number of characters left before the user reaches the length limit.

Authored by [Basil Shubin](https://github.com/bashu)

[![Latest Version](https://img.shields.io/pypi/v/django-charsleft-widget.svg)](https://pypi.python.org/pypi/django-charsleft-widget/)
[![Downloads](https://img.shields.io/pypi/dm/django-charsleft-widget.svg)](https://pypi.python.org/pypi/django-charsleft-widget/)
[![License](https://img.shields.io/github/license/bashu/django-charsleft-widget.svg)](https://pypi.python.org/pypi/django-charsleft-widget/)
[![Build Status](https://img.shields.io/travis/bashu/django-charsleft-widget.svg)](https://travis-ci.org/bashu/django-charsleft-widget/)

## Installation
```shell
$ pip install django-charsleft-widget
```
### External dependencies

* jQuery - This is not included in the package since it is expected that in most scenarios this would already be available.

## Setup

Add `charsleft_widget` to  `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
	...
	'charsleft_widget',
]
```
and just include `charsleft_widget` templates
```html
{% include "charsleft_widget/charsleft_widget_css.html" %} {# Before the closing head tag #}
{% include "charsleft_widget/charsleft_widget_js.html" %} %} {# Before the closing body tag #}
```
When deploying on production server, don't forget to run :
```shell
$ python manage.py collectstatic
```
## Usage

All you need now is to import ``CharsLeftArea`` class and override field's widget, for example :
```python
import django
if django.VERSION < (1,7):
    from charsleft_widget.fields import CharField
else:
    from django.forms.fields import CharField

from charsleft_widget import CharsLeftArea


class Form(forms.Form):

    field = CharField(max_length=128, widget=CharsLeftArea)
```
Please see `example` application. This application is used to manually test the functionalities of this package. This also serves as a good example.

You need only Django 1.4 or above to run that. It might run on older versions but that is not tested.

## License

`django-charsleft-widget` is released under the BSD license.
