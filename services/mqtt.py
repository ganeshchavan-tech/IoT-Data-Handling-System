import pika
from common.constants import *
from .logging import logger

# Function to start the consumer
def connect_to_rabbitmq():
    try:
        # Connect to RabbitMQ
        credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
        parameters = pika.ConnectionParameters(RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_VIRTUAL_HOST, credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        logger.info("Successfully connected to RabbitMQ")
        return channel
    
    except Exception as e:
        logger.error(f"Error connecting to RabbitMQ: {e}")
        return None

