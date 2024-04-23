from django.conf import settings
from django.contrib import admin


class CustomModalAdmin(admin.ModelAdmin):
    class Media:
        extra = "" if settings.DEBUG else ".min"
        js = [
            "admin/js/vendor/jquery/jquery%s.js" % extra,
            "admin/js/jquery.init.js",
            "js/jquery-ui.min.js",
            "js/custom_modal_admin.js",
        ]
        css = {
            "all": ("css/jquery-ui.css",),
        }
