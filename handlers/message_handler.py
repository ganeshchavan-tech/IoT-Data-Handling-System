import json
from services import connect_to_rabbitmq, logger
from utils import store_message, QUEUE_NAME

# Function to process the messages
def process_message(channel, method, properties, body):
    try:
        # Decode message body (JSON format)
        message = json.loads(body.decode('utf-8'))
        logger.info(f"Received message: {message}")
        
        store_message(message)
        logger.info(f"Message successfully stored.")

        # Acknowledgement of message delivery
        channel.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        logger.error(f"Error processing message: {e}")


# Function to start message consumer
def start_message_consumer():
    channel = connect_to_rabbitmq()
    
    # queue declaration
    channel.queue_declare(queue=QUEUE_NAME, durable=True)

    # message consumer
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=process_message)
    logger.info("Waiting for messages. To exit press CTRL+C")

    # consuming messages
    channel.start_consuming()
