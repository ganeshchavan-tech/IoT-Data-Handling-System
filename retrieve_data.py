from utils.connections import connect_to_mongodb
from services import logger
from common.constants import *

def retrieve_data_from_mongodb(query={}):
    try:
        collection = connect_to_mongodb(DATABASE_NAME, COLLECTION_NAME)
        # Retrieve data from MongoDB collection
        cursor = collection.find(query)
        # logger.info("Data retrieved from MongoDB")

        # Convert cursor to list of documents
        data = list(cursor)

        return data

    except Exception as e:
        logger.error(f"Error retrieving data from MongoDB: {e}")
        return None
    
if __name__ == "__main__":
    print(retrieve_data_from_mongodb())