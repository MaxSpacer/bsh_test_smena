from django.apps import AppConfig

class PolledConfig(AppConfig):
    name = 'polled'
    # verbose_name = 'Заказы'
    def ready(self):
        import polled.signals 
