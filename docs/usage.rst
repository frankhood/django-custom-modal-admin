=====
Usage
=====

To use Django custom modal admin in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'custom_modal_admin.apps.CustomModalAdminConfig',
        ...
    )

Add Django custom modal admin's URL patterns:

.. code-block:: python

    from custom_modal_admin import urls as custom_modal_admin_urls


    urlpatterns = [
        ...
        url(r'^', include(custom_modal_admin_urls)),
        ...
    ]
