# -*- coding: utf-8 -*-
from django.contrib import admin


class CustomModalAdmin(admin.ModelAdmin):

    class Media:
        js = [
            "admin/js/vendor/jquery/jquery.js",
            'admin/js/jquery.init.js',
            "js/jquery-ui.min.js",
            'js/custom_modal_admin.js',
        ]
        css = {
            'all': (
                "css/jquery-ui.css",
            ),
        }