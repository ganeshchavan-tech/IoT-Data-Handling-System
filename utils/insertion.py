from .connections import connect_to_mongodb
from common.constants import *
from services import logger

# Function to insert message into MongoDB
def insert_message(collection, message):
    try:
        # Insert the message into the collection
        collection.insert_one(message)
        logger.info("Message inserted successfully!")

    except Exception as e:
        logger.error(f"Error inserting message into MongoDB: {e}")


# Insertion function
def store_message(message):
    # Connect to MongoDB and create database/collection if they don't exist
    collection = connect_to_mongodb(DATABASE_NAME, COLLECTION_NAME)

    # Insert sample message into MongoDB
    insert_message(collection, message)
