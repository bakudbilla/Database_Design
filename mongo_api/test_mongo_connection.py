from pymongo import MongoClient

# MongoDB connection string
MONGO_URI = "mongodb+srv://kmugisha:kmugisha@cluster0.zusx7.mongodb.net/<TitanicDB>?retryWrites=true&w=majority&appName=Cluster0"

try:
    # Connect to MongoDB
    client = MongoClient(MONGO_URI)

    # Test the connection
    db = client.get_database()
    print("Connected to MongoDB!")
    print("Collections in the database:", db.list_collection_names())
except Exception as e:
    print("Error connecting to MongoDB:", e)