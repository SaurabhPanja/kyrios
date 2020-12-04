from django.apps import AppConfig


class JugaadConfig(AppConfig):
    name = 'jugaad'

    def ready(self):
        import jugaad.signals
