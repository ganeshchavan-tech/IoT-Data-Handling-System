import pymongo
from .constants import *
from services.logging import logger

def connect_to_mongodb(database_name, collection_name):
    try:
        # Connect to MongoDB server
        client = pymongo.MongoClient(MONGO_DB_URI)
        logger.info("Successfully connected to MongoDB")

        # Setup database
        db = client[database_name]
        logger.info(f"Using database: {database_name}")

        # Setup collection
        collection = db[collection_name]
        logger.info(f"Using collection: {collection_name}")

        return collection

    except Exception as e:
        logger.error(f"Error connecting to MongoDB: {e}")
        return None
