from django.db import models
from . import managers as app_managers
from . import querysets as app_querysets


class ExampleModel(models.Model):
    objects = app_managers.ExampleModelManager.from_queryset(app_querysets.ExampleModelQuerySet)()

    title = models.CharField("Title", max_length=255)
    subtitle = models.CharField("Subtitle", max_length=255, default="", blank=True)
    description = models.CharField("Description", max_length=255, default="", blank=True)

    class Meta:
        """ExampleModel Meta."""

        verbose_name = "ExampleModel"
        verbose_name_plural = "ExampleModels"

    def __str__(self) -> str:
        return self.title
