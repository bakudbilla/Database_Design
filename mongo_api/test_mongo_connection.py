from pymongo import MongoClient

# MongoDB connection string
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URL")
try:
    # Connect to MongoDB
    client = MongoClient(MONGO_URI)

    # Test the connection
    db = client.get_database()
    print("Connected to MongoDB!")
    print("Collections in the database:", db.list_collection_names())
except Exception as e:
    print("Error connecting to MongoDB:", e)