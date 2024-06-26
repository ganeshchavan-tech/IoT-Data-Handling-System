# IoT Data Handling System

## Description
The IoT Data Handling System efficiently processes and stores MQTT messages using Python, RabbitMQ, and MongoDB. This project facilitates seamless integration of message handling and storage, making it ideal for IoT applications.

## Requirements
Ensure you have the following prerequisites and dependencies installed to run the script:

- Python 3.x
- RabbitMQ ([Download](https://www.rabbitmq.com/docs/download))
- Pika (RabbitMQ client library for Python)
- PyMongo (Python driver for MongoDB)
- MongoDB database

## Installation
Follow these step-by-step instructions to install the required dependencies and set up the environment:

1. Clone the repository:
   ```
   git clone https://github.com/ganeshchavan-tech/IoT-Data-Handling-System.git
   ```

2. Navigate to the project directory:
   ```
   cd project_directory
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

### Environment Variables:
Set the following environment variables for RabbitMQ connection parameters:

- RABBITMQ_HOST
- RABBITMQ_PORT
- RABBITMQ_USERNAME
- RABBITMQ_PASSWORD
- RABBITMQ_VIRTUAL_HOST
- MQTT_EXCHANGE
- QUEUE_NAME

For MongoDB configuration, set:

- MONGO_DB_URI
- DATABASE_NAME
- COLLECTION_NAME

## Usage
Follow these detailed steps to run the Python script:

1. Ensure you have completed the installation and configuration steps.
2. Run the script using the following command:
   ```
   python main.py
   ```

## Unit Tests

This project includes unit tests to ensure the correctness and robustness of individual components and functions.

## Test Cases and Results

### Integration Test

- **Test Case:** Verify seamless integration of MQTT message processing from RabbitMQ to MongoDB.
- **Result:** Successful integration demonstrated by publishing a test message, processing it through the message handler, and storing it in MongoDB.

### Manual Test
- First, run the publisher.py script to publish the message.
- Then, execute the main.py script to retrieve and store the messages.
- Finally, run the retrieve_data.py script to retrieve stored data.

## Author
Ganesh Chavan