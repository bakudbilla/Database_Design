import requests
import pickle
import numpy as np
import json

# API endpoint to fetch the latest passenger entry
API_URL = "http://127.0.0.1:8000/api/passengers"
MODEL_PATH = "Fetch_and_Prediction/logistic_regression_model.pkl"

def fetch_latest_entry():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        if data:
            return data[-1]  # Get the latest entry
        else:
            print("No data found!")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def load_model():
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)
    return model

def prepare_data(passenger):
    # Extract relevant features (adjust as per your model's input requirements)
    features = [
        passenger["Age"],
        passenger["SibSp"],
        passenger["Parch"],
        passenger["TicketId"],
    ]
    return np.array(features).reshape(1, -1)

def predict_survival(model, input_data):
    prediction = model.predict(input_data)
    return "Survived" if prediction[0] == 1 else "Not Survived"

def main():
    passenger = fetch_latest_entry()
    if passenger:
        model = load_model()
        input_data = prepare_data(passenger)
        result = predict_survival(model, input_data)
        print(f"Prediction for Passenger {passenger['PassengerId']}: {result}")

if __name__ == "__main__":
    main()
