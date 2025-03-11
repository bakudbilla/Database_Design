from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URI)

db = client["TitanicDB"]

print("Collections in TitanicDB:", db.list_collection_names())


# creating Passengers collection and loading the data from Passengers.csv
passengers = pd.read_csv("./data/Passengers.csv")

passenger_records = passengers.to_dict(orient="records")
db.passengers.insert_many(passenger_records)

# creating Tickets collection and loading the data from Tickets.csv
tickets = pd.read_csv("./data/Tickets.csv")

ticket_records = tickets.to_dict(orient="records")
db.tickets.insert_many(ticket_records)

# creating Survivors collection and loading the data from Survivors.csv
survivors = pd.read_csv("./data/Survivors.csv")

survivor_records = survivors.to_dict(orient="records")
db.survivors.insert_many(survivor_records)
