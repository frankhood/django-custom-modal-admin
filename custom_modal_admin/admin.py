# -*- coding: utf-8 -*-
from django.contrib import admin


class CustomModalAdmin(admin.ModelAdmin):

    class Media:
        js = [
            'https://code.jquery.com/jquery-2.2.4.min.js',
            'https://code.jquery.com/ui/1.12.1/jquery-ui.min.js',
            'admin/js/custom_modal_admin.js',
        ]
        css = {
            'all': (
                'https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css',
            ),
        }