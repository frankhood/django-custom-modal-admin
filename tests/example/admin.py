from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import ExampleModel


@admin.register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "description", "display_toggle_modal")
    readonly_fields = ("display_toggle_modal",)

    fieldsets = (
        (
            None,
            {
                "fields": (
                    ("title", "subtitle", "description"),
                    ("display_toggle_modal",),
                )
            },
        ),
    )

    @mark_safe
    def display_toggle_modal(self, obj):
        return """
            <input
                class='js-django-admin-custom-modal'
                type='button'
                data-target-name='load-template-modal'
                value='Click to show modal'
                name='_load_modal'
            >
            <div data-django-admin-custom-modal="load-template-modal" style="display:none;">
                <span>This is a modal</span>
            </div>
        """
