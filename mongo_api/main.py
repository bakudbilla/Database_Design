from fastapi import FastAPI, HTTPException
from models import (
    PassengerCreate, PassengerDB,
    TicketCreate, TicketDB,
    SurvivorCreate, SurvivorDB
)
from database import passengers_collection, tickets_collection, survivors_collection

app = FastAPI()

# Helper function to serialize MongoDB document
def serialize_doc(doc):
    if doc:
        doc["_id"] = str(doc["_id"])  
    return doc

# CRUD for Passengers
@app.post("/passengers/", response_model=PassengerDB)
async def create_passenger(passenger: PassengerCreate):
    passenger_dict = passenger.model_dump()
    result = passengers_collection.insert_one(passenger_dict)
    new_passenger = passengers_collection.find_one({"_id": result.inserted_id})
    return serialize_doc(new_passenger)

@app.get("/passengers/{passenger_id}", response_model=PassengerDB)
async def read_passenger(passenger_id: int):
    passenger = passengers_collection.find_one({"PassengerId": passenger_id})
    if passenger:
        return serialize_doc(passenger)
    raise HTTPException(status_code=404, detail="Passenger not found")

@app.put("/passengers/{passenger_id}", response_model=PassengerDB)
async def update_passenger(passenger_id: int, passenger: PassengerCreate):
    result = passengers_collection.update_one(
        {"PassengerId": passenger_id}, {"$set": passenger.dict()}
    )
    if result.modified_count:
        updated_passenger = passengers_collection.find_one({"PassengerId": passenger_id})
        return serialize_doc(updated_passenger)
    raise HTTPException(status_code=404, detail="Passenger not found")

@app.delete("/passengers/{passenger_id}")
async def delete_passenger(passenger_id: int):
    result = passengers_collection.delete_one({"PassengerId": passenger_id})
    if result.deleted_count:
        return {"message": "Passenger deleted successfully"}
    raise HTTPException(status_code=404, detail="Passenger not found")

# CRUD for Tickets
@app.post("/tickets/", response_model=TicketDB)
async def create_ticket(ticket: TicketCreate):
    ticket_dict = ticket.dict()
    result = tickets_collection.insert_one(ticket_dict)
    new_ticket = tickets_collection.find_one({"_id": result.inserted_id})
    return serialize_doc(new_ticket)

@app.get("/tickets/{ticket_id}", response_model=TicketDB)
async def read_ticket(ticket_id: int):
    ticket = tickets_collection.find_one({"TicketId": ticket_id})
    if ticket:
        return serialize_doc(ticket)
    raise HTTPException(status_code=404, detail="Ticket not found")

@app.put("/tickets/{ticket_id}", response_model=TicketDB)
async def update_ticket(ticket_id: int, ticket: TicketCreate):
    result = tickets_collection.update_one(
        {"TicketId": ticket_id}, {"$set": ticket.dict()}
    )
    if result.modified_count:
        updated_ticket = tickets_collection.find_one({"TicketId": ticket_id})
        return serialize_doc(updated_ticket)
    raise HTTPException(status_code=404, detail="Ticket not found")

@app.delete("/tickets/{ticket_id}")
async def delete_ticket(ticket_id: int):
    result = tickets_collection.delete_one({"TicketId": ticket_id})
    if result.deleted_count:
        return {"message": "Ticket deleted successfully"}
    raise HTTPException(status_code=404, detail="Ticket not found")

# CRUD for Survivors
@app.post("/survivors/", response_model=SurvivorDB)
async def create_survivor(survivor: SurvivorCreate):
    survivor_dict = survivor.dict()
    result = survivors_collection.insert_one(survivor_dict)
    new_survivor = survivors_collection.find_one({"_id": result.inserted_id})
    return serialize_doc(new_survivor)

@app.get("/survivors/{survivor_id}", response_model=SurvivorDB)
async def read_survivor(survivor_id: int):
    survivor = survivors_collection.find_one({"SurvivorId": survivor_id})
    if survivor:
        return serialize_doc(survivor)
    raise HTTPException(status_code=404, detail="Survivor not found")

@app.put("/survivors/{survivor_id}", response_model=SurvivorDB)
async def update_survivor(survivor_id: int, survivor: SurvivorCreate):
    result = survivors_collection.update_one(
        {"SurvivorId": survivor_id}, {"$set": survivor.model_dump()}
    )
    if result.modified_count:
        updated_survivor = survivors_collection.find_one({"SurvivorId": survivor_id})
        return serialize_doc(updated_survivor)
    raise HTTPException(status_code=404, detail="Survivor not found")

@app.delete("/survivors/{survivor_id}")
async def delete_survivor(survivor_id: int):
    result = survivors_collection.delete_one({"SurvivorId": survivor_id})
    if result.deleted_count:
        return {"message": "Survivor deleted successfully"}
    raise HTTPException(status_code=404, detail="Survivor not found")