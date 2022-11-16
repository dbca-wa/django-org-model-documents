from django.apps import AppConfig
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


class OrgModelDocumentsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "org_model_documents"
    verbose_name = "Org Model Documents"

    def ready(self):
        if (
            not hasattr(settings, "ORG_MODEL_DOCUMENTS_MEDIA_ROOT")
            or not settings.ORG_MODEL_DOCUMENTS_MEDIA_ROOT
        ):
            raise ImproperlyConfigured(
                "ORG_MODEL_DOCUMENTS_MEDIA_ROOT is not set in settings.py"
            )
