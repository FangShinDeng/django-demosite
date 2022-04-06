from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_account'

    def ready(self) -> None:
        import custom_account.signals