Changes
-------

1.1.0 (2026-08-14)
~~~~~~~~~~~~~~~~~~

* Added Django 6.0 and 6.1 support, alongside existing Django 5.2 support (fixes #7).
* Dropped Python < 3.10 support.
* Fixed ``charsleft.js``: a page without both jQuery and a ``django`` global
  crashed with ``ReferenceError: django is not defined``; typing past
  ``maxlength`` right on an emoji or other astral character split its UTF-16
  surrogate pair and corrupted the field; only ``keyup``/``change`` were
  handled, so paste-via-mouse and IME input didn't update the count;
  dynamically-added widgets (formsets, ajax) were never wired up; and the
  ``charsleft`` helper leaked onto ``window``.
* Fixed ``USE_JINJA`` rendering: ``textarea.jinja`` lived under
  ``templates/``, where Django's Jinja2 backend (``APP_DIRS`` scans each
  app's ``jinja2/`` directory) could never find it; moved it to
  ``charsleft_widget/jinja2/``.
* Removed ``charsleft_widget/fields.py``, a pre-Django-1.7 ``maxlength``
  shim superseded by Django core and unused since.
* ``locale/`` and ``jinja2/`` assets weren't declared in ``package-data``
  and were silently missing from built wheels/sdists; added.
* Increased test coverage to 100%; added tests for ``Media``, a value
  already over ``maxlength``, and the Jinja2 backend actually being used.
* Reformatted code and templates, and fixed ruff lint findings.

1.0.0 (2021-11-30)
~~~~~~~~~~~~~~~~~~

* Added Django 3+ support.
* Dropped Python 2.7 support.
* Dropped Django 1.10 / 1.11 support.
