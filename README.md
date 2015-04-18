django-charsleft-widget
===

django-charsleft-widget is a custom widget that limits the number of characters that can be entered in a textarea  field. The widget can also report the number of characters left before the user reaches the length limit.

[![Latest Version](https://pypip.in/version/django-charsleft-widget/badge.svg)](https://pypi.python.org/pypi/django-charsleft-widget/)
[![Downloads](https://pypip.in/download/django-charsleft-widget/badge.svg)](https://pypi.python.org/pypi/django-charsleft-widget/)
[![License](https://pypip.in/license/django-charsleft-widget/badge.svg)](https://pypi.python.org/pypi/django-charsleft-widget/)

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
from charsleft_widget import CharsLeftArea

class Form(forms.Form):

    field = forms.CharField(max_length=128, widget=CharsLeftArea)
```
Please see `example` application. This application is used to manually test the functionalities of this package. This also serves as a good example.

You need only Django 1.4 or above to run that. It might run on older versions but that is not tested.

## License

`django-charsleft-widget` is authored by [Basil Shubin](http://resume.github.io/?bashu) and released under the BSD license.
