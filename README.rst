django-clearable-widget
=======================

django-clearable-widget is a custom widget that adds a input clearing
button on any input fields that are using it. It clears the value, and
returns focus to that field.

Authored by `Basil Shubin <https://github.com/bashu>`_

.. image:: https://img.shields.io/pypi/v/django-clearable-widget.svg
    :target: https://pypi.python.org/pypi/django-clearable-widget/

.. image:: https://img.shields.io/pypi/dm/django-clearable-widget.svg
    :target: https://pypi.python.org/pypi/django-clearable-widget/

.. image:: https://img.shields.io/github/license/bashu/django-clearable-widget.svg
    :target: https://pypi.python.org/pypi/django-clearable-widget/

.. image:: https://img.shields.io/travis/bashu/django-clearable-widget.svg
    :target: https://travis-ci.org/bashu/django-clearable-widget/

.. image:: https://landscape.io/github/bashu/django-clearable-widget/develop/landscape.svg?style=flat
    :target: https://landscape.io/github/bashu/django-clearable-widget/develop

Installation
------------

.. code-block:: bash

    pip install django-clearable-widget

External dependencies
~~~~~~~~~~~~~~~~~~~~~

* jQuery - this is not included in the package since it is expected
  that in most scenarios this would already be available.

Setup
-----

Add ``clearable_widget`` to  ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS += (
        'clearable_widget',
    )

and just include ``clearable_widget`` templates

.. code-block:: html+django

    {% include "clearable_widget/clearable_widget_css.html" %} {# Before the closing head tag #}
    {% include "clearable_widget/clearable_widget_js.html" %} %} {# Before the closing body tag #}

When deploying on production server, don't forget to run:

.. code-block:: shell

    python manage.py collectstatic

Usage
-----

All you need now is to import ``ClearableInput`` class and override
field's widget, for example:

.. code-block:: python

    from clearable_widget import ClearableInput

    class Form(forms.Form):

        field = forms.CharField(widget=ClearableInput)

Please see ``example`` application. This application is used to
manually test the functionalities of this package. This also serves as
a good example.

You need only Django 1.4 or above to run that. It might run on older
versions but that is not tested.

License
-------

``django-clearable-widget`` is released under the BSD license.
