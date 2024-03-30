import unittest
from unittest.mock import patch, MagicMock
import json
from ..publisher import publish_message
from handlers.message_handler import process_message

class TestIntegration(unittest.TestCase):

    @patch('services.mqtt.connect_to_rabbitmq')
    @patch('utils.connections.connect_to_mongodb')
    @patch('publish_message.publish_message')
    def test_integration(self, mock_publish, mock_connect_to_mongodb, mock_connect_to_rabbitmq):
        # Mocking RabbitMQ connection
        mock_channel = MagicMock()
        mock_channel.basic_consume.return_value = None
        mock_connect_to_rabbitmq.return_value = mock_channel

        # Mocking MongoDB connection
        mock_collection = MagicMock()
        mock_connect_to_mongodb.return_value = mock_collection

        # Publishing a test message
        test_topic = "test/topic"
        test_payload = {"test_message": "Hello, MQTT!"}
        publish_message(test_topic, json.dumps(test_payload))
        mock_publish.assert_called_once_with(test_topic, json.dumps(test_payload), hostname="localhost", port=1883)

        # Simulating message consumption
        test_message = json.dumps(test_payload).encode('utf-8')
        process_message(mock_channel, MagicMock(), MagicMock(), test_message)
        mock_collection.insert_one.assert_called_once_with(test_payload)

if __name__ == '__main__':
    unittest.main()
