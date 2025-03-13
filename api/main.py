from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import Database_Design.api.crud as crud, schemas
from Database_Design.api.database import get_db

app = FastAPI()

# Passenger Endpoints
@app.post("/passengers/", response_model=schemas.PassengerResponse)
def create_passenger(passenger: schemas.PassengerCreate, db: Session = Depends(get_db)):
    return crud.create_passenger(db, passenger)

@app.get("/passengers/", response_model=list[schemas.PassengerResponse])
def get_all_passengers(db: Session = Depends(get_db)):
    return crud.get_passengers(db)

@app.get("/passengers/{passenger_id}", response_model=schemas.PassengerResponse)
def get_passenger(passenger_id: int, db: Session = Depends(get_db)):
    passenger = crud.get_passenger(db, passenger_id)
    if not passenger:
        raise HTTPException(status_code=404, detail="Passenger not found")
    return passenger

@app.put("/passengers/{passenger_id}", response_model=schemas.PassengerResponse)
def update_passenger(passenger_id: int, passenger: schemas.PassengerCreate, db: Session = Depends(get_db)):
    updated_passenger = crud.update_passenger(db, passenger_id, passenger)
    if not updated_passenger:
        raise HTTPException(status_code=404, detail="Passenger not found")
    return updated_passenger

@app.delete("/passengers/{passenger_id}")
def delete_passenger(passenger_id: int, db: Session = Depends(get_db)):
    deleted_passenger = crud.delete_passenger(db, passenger_id)
    if not deleted_passenger:
        raise HTTPException(status_code=404, detail="Passenger not found")
    return {"message": "Passenger deleted successfully"}

# Survivor Endpoints
@app.post("/survivors/", response_model=schemas.SurvivorResponse)
def create_survivor(survivor: schemas.SurvivorCreate, db: Session = Depends(get_db)):
    new_survivor = crud.create_survivor(db, survivor)
    if not new_survivor:
        raise HTTPException(status_code=404, detail="Passenger not found")
    return new_survivor

@app.get("/survivors/", response_model=list[schemas.SurvivorResponse])
def get_all_survivors(db: Session = Depends(get_db)):
    return crud.get_survivors(db)

@app.get("/survivors/{passenger_id}", response_model=schemas.SurvivorResponse)
def get_survivor(passenger_id: int, db: Session = Depends(get_db)):
    survivor = crud.get_survivor(db, passenger_id)
    if not survivor:
        raise HTTPException(status_code=404, detail="Survivor not found")
    return survivor

@app.put("/survivors/{passenger_id}", response_model=schemas.SurvivorResponse)
def update_survivor(passenger_id: int, survivor: schemas.SurvivorCreate, db: Session = Depends(get_db)):
    updated_survivor = crud.update_survivor(db, passenger_id, survivor)
    if not updated_survivor:
        raise HTTPException(status_code=404, detail="Survivor not found")
    return updated_survivor

@app.delete("/survivors/{passenger_id}")
def delete_survivor(passenger_id: int, db: Session = Depends(get_db)):
    deleted_survivor = crud.delete_survivor(db, passenger_id)
    if not deleted_survivor:
        raise HTTPException(status_code=404, detail="Survivor not found")
    return {"message": "Survivor deleted successfully"}

# Ticket Endpoints
@app.post("/tickets/", response_model=schemas.TicketResponse)
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    new_ticket = crud.create_ticket(db, ticket)
    if not new_ticket:
        raise HTTPException(status_code=404, detail="Passenger not found")
    return new_ticket

@app.get("/tickets/", response_model=list[schemas.TicketResponse])
def get_all_tickets(db: Session = Depends(get_db)):
    return crud.get_tickets(db)

@app.get("/tickets/{ticket_id}", response_model=schemas.TicketResponse)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = crud.get_ticket(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@app.put("/tickets/{ticket_id}", response_model=schemas.TicketResponse)
def update_ticket(ticket_id: int, ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    updated_ticket = crud.update_ticket(db, ticket_id, ticket)
    if not updated_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return updated_ticket

@app.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    deleted_ticket = crud.delete_ticket(db, ticket_id)
    if not deleted_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {"message": "Ticket deleted successfully"}
