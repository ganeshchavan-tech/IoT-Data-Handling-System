import pika
from common.constants import *
from services import connect_to_rabbitmq

def publish_message(payload):
    try:
        channel = connect_to_rabbitmq()

        # Publish message
        channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=payload)

        print(f"Published message to topic '{QUEUE_NAME}': {payload}")
    
    except Exception as e:
        print(f"Failed to publish message: {e}")


if __name__ == "__main__":
    publish_message('{"test_message2": "Hello, MQTT!"}')
