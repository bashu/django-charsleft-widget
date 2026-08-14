django-charsleft-widget
=======================

.. image:: https://badge.fury.io/py/django-charsleft-widget.svg
    :target: https://badge.fury.io/py/django-charsleft-widget

.. image:: https://img.shields.io/pypi/pyversions/django-charsleft-widget.svg
    :target: https://pypi.python.org/pypi/django-charsleft-widget/

.. image:: https://img.shields.io/pypi/djversions/django-charsleft-widget.svg
    :target: https://pypi.python.org/pypi/django-charsleft-widget/

.. image:: https://github.com/bashu/django-charsleft-widget/actions/workflows/test.yml/badge.svg
    :target: https://github.com/bashu/django-charsleft-widget/actions/workflows/test.yml

django-charsleft-widget is a custom widget that limits the number of characters that can be entered in a textarea field.

.. image:: https://raw.githubusercontent.com/bashu/django-charsleft-widget/develop/showcase.gif
   :target: https://raw.githubusercontent.com/bashu/django-charsleft-widget/develop/showcase.gif
   :align: center
   :width: 600px

Installation
------------

.. code-block:: bash

    pip install django-charsleft-widget

External dependencies
~~~~~~~~~~~~~~~~~~~~~

* jQuery - this is not included in the package since it is expected
  that in most scenarios this would already be available.

Setup
-----

Add ``charsleft_widget`` to  ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS += (
        'charsleft_widget',
    )

and just include ``charsleft_widget`` templates

.. code-block:: html+django

    {% include "charsleft_widget/charsleft_widget_css.html" %} {# Before the closing head tag #}
    {% include "charsleft_widget/charsleft_widget_js.html" %} {# Before the closing body tag #}

When deploying on production server, don't forget to run:

.. code-block:: shell

    python manage.py collectstatic

Usage
-----

All you need now is to import ``ClearableInput`` class and override
field's widget, for example:

.. code-block:: python

    from django.forms.fields import CharField

    from charsleft_widget import CharsLeftArea

    class Form(forms.Form):

        field = CharField(max_length=128, widget=CharsLeftArea)

Please see ``example`` application. This application is used to
manually test the functionalities of this package. This also serves as
a good example.

You need only Django 1.4 or above to run that. It might run on older
versions but that is not tested.

License
-------

``django-charsleft-widget`` is released under the BSD license.
