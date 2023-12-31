import base64
import json

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = json.loads(base64.b64decode(event['data']).decode('utf-8'))
    timestamp = pubsub_message['timestamp']
    remoteIp = pubsub_message['httpRequest']['remoteIp']
    userAgent = pubsub_message['httpRequest']['userAgent']

    print(remoteIp)
    print(userAgent)
