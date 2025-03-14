import numpy as np
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import pickle

# Load environment variables
load_dotenv()

# Load the pre-trained model
with open('logistic_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URI)
db = client["TitanicDB"]  # Replace with your database name

# Function to fetch the latest data from MongoDB
def fetch_latest_data(collection_name):
    try:
        # Fetch the latest document from the collection
        latest_data = db[collection_name].find_one(sort=[("_id", -1)])
        if latest_data:
            print(f"Fetched data from {collection_name}:", latest_data)
            return latest_data
        else:
            print(f"No data found in {collection_name}")
            return None
    except Exception as e:
        print(f"Error fetching data from {collection_name}: {e}")
        return None

# Function to preprocess the data
def preprocess_data(passenger_data, ticket_data, survivor_data):
    # Mapping for categorical variables (if needed)
    gender_map = {"female": 0, "male": 1}
    embarked_map = {"S": 0, "C": 1, "Q": 2}

    # Extract features and preprocess them in the correct order
    preprocessed_data = [
        # Passenger data
        passenger_data.get("Pclass", 0),
        gender_map.get(passenger_data.get("Sex", "").lower(), 0),  # Encode gender
        passenger_data.get("Age", 0.0),
        passenger_data.get("SibSp", 0),
        passenger_data.get("Parch", 0),
        # Ticket data
        ticket_data.get("Fare", 0.0),
        embarked_map.get(ticket_data.get("Embarked", ""), 0),  # Encode embarked
    ]

    # Return the preprocessed data in the required order
    return preprocessed_data

# Function to make predictions
def make_prediction(preprocessed_data):
    prediction = model.predict(np.array([preprocessed_data]))
    return prediction

if __name__ == "__main__":
    # Fetch the latest data from MongoDB collections
    passenger_data = fetch_latest_data("passengers")
    ticket_data = fetch_latest_data("tickets")
    survivor_data = fetch_latest_data("survivors")

    if passenger_data and ticket_data and survivor_data:
        # Preprocess the data
        preprocessed_data = preprocess_data(passenger_data, ticket_data, survivor_data)
        print("Preprocessed data:", preprocessed_data)

        # Make a prediction
        prediction = make_prediction(preprocessed_data)
        prediction = 0 if prediction < 0.5 else 1
        print("Prediction:", prediction)
    else:
        print("Failed to fetch data from one or more collections.")
