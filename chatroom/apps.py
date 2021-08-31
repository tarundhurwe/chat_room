from django.apps import AppConfig


class ChatroomConfig(AppConfig):
    name = 'chatroom'

    def ready(self):
        from jobs import updater
        updater.start()