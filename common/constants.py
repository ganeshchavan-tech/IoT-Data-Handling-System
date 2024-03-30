import os

# RabbitMQ connection parameters
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
RABBITMQ_PORT = int(os.getenv('RABBITMQ_PORT', 5672))
RABBITMQ_USERNAME = os.getenv('RABBITMQ_USERNAME', 'guest')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD', 'guest')
RABBITMQ_VIRTUAL_HOST = os.getenv('RABBITMQ_VIRTUAL_HOST', '/')
MQTT_EXCHANGE = os.getenv('MQTT_EXCHANGE', 'amq.topic')
QUEUE_NAME = os.getenv('QUEUE_NAME', 'mqtt_queue')

# MongoDB Config
MONGO_DB_URI = os.getenv('MONGO_DB_URI', 'mongodb://localhost:27017/')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'iot_data')
COLLECTION_NAME = os.getenv('COLLECTION_NAME', 'mqtt_messages')
