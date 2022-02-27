from django.apps import AppConfig

class HospitalConfig(AppConfig):
    name = 'Hospital'

    def ready(self):
        # noinspection PyUnresolvedReferences
        import Hospital.signals