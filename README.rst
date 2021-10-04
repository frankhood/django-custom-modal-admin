=============================
Django custom modal admin
=============================

.. image:: https://badge.fury.io/py/django-custom-modal-admin.svg
    :target: https://badge.fury.io/py/django-custom-modal-admin

.. image:: https://travis-ci.org/frankhood/django-custom-modal-admin.svg?branch=master
    :target: https://travis-ci.org/frankhood/django-custom-modal-admin

.. image:: https://codecov.io/gh/frankhood/django-custom-modal-admin/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/frankhood/django-custom-modal-admin

Your project description goes here

Documentation
-------------

The full documentation is at https://django-custom-modal-admin.readthedocs.io.

Quickstart
----------

Install Django custom modal admin::

    pip install django-custom-modal-admin

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'custom_modal_admin',
        ...
    )

Override CustomModalAdmin in your model admin:

.. code-block:: python

    @admin.register(ExampleModel)
    class ExampleModelAdmin(CustomModalAdmin, admin.ModelAdmin):
        list_display = ("title", "subtitle", "description",)

        fieldsets = (
            (None, {"fields": (
                ("title", "subtitle", "description")
            )}),
        )

This admin add to your class Media this dependencies:

.. code-block:: python

    class Media:
        js = [
            'https://code.jquery.com/jquery-2.2.4.min.js',
            'https://code.jquery.com/ui/1.12.1/jquery-ui.min.js',
            'js/custom_modal_admin.js',
        ]
        css = {
            'all': (
                'https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css',
            ),
        }

take care of this media when override Media class.

To display the modal insert in your templates a target html tag, using django admin or adding it in template or wherever you want, for example:

.. code-block:: html

    <input 
        class='js-django-admin-custom-modal' // this class is required
        data-target-name='load-template-modal' // this target name is required
        type='button' 
        value='Click to show modal'
    >

and the template of your modal with custom content:

.. code-block:: html

    <div data-django-admin-custom-modal="load-template-modal" style="display:none;">
        <span>This is a modal</span>
    </div>

Now you can insert whatever you want in that modal.

You can also insert in the same block or display_field the admin and the button, for example:

.. code-block:: html

    <input 
        class='js-django-admin-custom-modal' 
        type='button' 
        data-target-name='load-template-modal' 
        value='Click to show modal' 
    >
    <div data-django-admin-custom-modal="load-template-modal" style="display:none;">
        <span>This is a modal</span>
    </div>

If you need to insert a modal for all your site, you can override base_site.html and insert in the extrastyle block
the required css.

.. code-block:: html

    {% block extrastyle %}
    {{ block.super }}
        <link rel="stylesheet" type="text/css" href="https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
    {% endblock %}

And the required js into extrahead block:

.. code-block:: html

    {% block extrahead %}
        <script src="https://code.jquery.com/jquery-2.2.4.min.js" defer></script>
        <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.min.js" defer></script>
        <script src="{% static 'js/custom_modal_admin.js' %}" defer></script>
    {% endblock %}


With this last implementation you can avoid to inerith CustomModalAdmin in all yours admin.


Features
--------

* Add a custom js to display easy modal in your django admin


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
