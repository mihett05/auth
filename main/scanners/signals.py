from django.dispatch import Signal, receiver
from asgiref.sync import async_to_sync

from channels import layers


command_open = Signal()


@receiver(command_open)
def scanner_command_observer(sender, uuid=None, user_id=None, **kwargs):
    layer = layers.get_channel_layer()
    async_to_sync(layer.group_send)("scanner_command_group", {
        "type": "events.open",
        "data": {
            "uuid": uuid,
            "user_id": user_id
        }
    })
