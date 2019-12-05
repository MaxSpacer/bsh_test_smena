from django.apps import AppConfig

class PolledConfig(AppConfig):
    name = 'polled'
    verbose_name = 'результаты'
    def ready(self):
        import polled.signals
