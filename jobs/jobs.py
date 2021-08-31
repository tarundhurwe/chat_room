from django.conf import settings
from chatroom.models import Room, Message
from time import time, sleep
from datetime import datetime, timezone

def auto_delete():
    try:
        print("running")
        rooms = Room.objects.all()
        length = len(rooms)
        for i in rooms:
            message = Message.objects.filter(room = i.id).last()
            last_message_time = message.date
            time_now = datetime.now(timezone.utc)
            time_delta = time_now - last_message_time
            total_seconds = time_delta.total_seconds()
            minutes = total_seconds/60
            if minutes > 5:
                data_to_be_deleted = Message.objects.filter(room = i.id)
                data_to_be_deleted.delete()

    except:
        pass
