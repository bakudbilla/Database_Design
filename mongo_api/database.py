from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URI)
db = client["TitanicDB"]

# Collections
passengers_collection = db["passengers"]
tickets_collection = db["tickets"]
survivors_collection = db["survivors"]