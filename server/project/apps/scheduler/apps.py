from django.apps import AppConfig
from django.db.models.signals import post_migrate


class SchedulerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.scheduler'

    def ready(self):
        from .seed_data import seed_data
        post_migrate.connect(seed_data, sender=self)
