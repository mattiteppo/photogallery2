from django.apps import AppConfig


class SmartgalleryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'smartgallery'

    def ready(self):
        from . import signals
