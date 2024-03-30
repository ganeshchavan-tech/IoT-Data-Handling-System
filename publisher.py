import pika
from common.constants import *

def publish_message(topic, payload):
    try:
        credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
        parameters = pika.ConnectionParameters(RABBITMQ_HOST, RABBITMQ_PORT, '/', credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.basic_publish(exchange='', routing_key=topic, body=payload)
        connection.close()
        print(f"Published message to topic '{topic}': {payload}")
    except Exception as e:
        print(f"Failed to publish message: {e}")


# publish_message("test/topic", {"test_message" : "Hello, MQTT!"})
