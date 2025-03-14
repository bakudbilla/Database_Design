# main.py
from fastapi import FastAPI, HTTPException
from typing import List
import logging
from database import get_db_connection
from models import Passenger, PassengerCreate, Ticket, TicketCreate, Survivor, SurvivorCreate

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Helper function to execute queries
def execute_query(query, params=None, fetch_one=False):
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params or ())
        if fetch_one:
            result = cursor.fetchone()
        else:
            result = cursor.fetchall()
        connection.commit()
        return result
    except Exception as e:
        logging.error(f"Error executing query: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Passengers CRUD
@app.get("/api/passengers", response_model=List[Passenger])
def get_passengers():
    query = "SELECT * FROM Passengers"
    return execute_query(query)

@app.get("/api/passengers/{passenger_id}", response_model=Passenger)
def get_passenger(passenger_id: int):
    query = """
        SELECT 
            PassengerId, 
            Name, 
            Sex, 
            Age, 
            SibSp, 
            Parch, 
            TicketId 
        FROM Passengers 
        WHERE PassengerId = %s
    """
    passenger = execute_query(query, (passenger_id,), fetch_one=True)
    if not passenger:
        raise HTTPException(status_code=404, detail="Passenger not found")
    return passenger

@app.post("/api/passengers", response_model=Passenger)
def create_passenger(passenger: PassengerCreate):
    query = """
        INSERT INTO Passengers (
            PassengerId, 
            Name, 
            Sex, 
            Age, 
            SibSp, 
            Parch, 
            TicketId
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    params = (
        passenger.PassengerId,
        passenger.Name,
        passenger.Sex,
        passenger.Age,
        passenger.SibSp,
        passenger.Parch,
        passenger.TicketId
    )
    execute_query(query, params)
    return passenger

@app.put("/api/passengers/{passenger_id}", response_model=Passenger)
def update_passenger(passenger_id: int, passenger: PassengerCreate):
    query = """
        UPDATE Passengers 
        SET 
            Name = %s, 
            Sex = %s, 
            Age = %s, 
            SibSp = %s, 
            Parch = %s, 
            TicketId = %s 
        WHERE PassengerId = %s
    """
    params = (
        passenger.Name,
        passenger.Sex,
        passenger.Age,
        passenger.SibSp,
        passenger.Parch,
        passenger.TicketId,
        passenger_id
    )
    execute_query(query, params)
    return {**passenger.model_dump(), "PassengerId": passenger_id}

@app.delete("/api/passengers/{passenger_id}")
def delete_passenger(passenger_id: int):
    query = "DELETE FROM Passengers WHERE PassengerId = %s"
    execute_query(query, (passenger_id,))
    return {"message": "Passenger deleted successfully"}

# Tickets CRUD
@app.get("/api/tickets", response_model=List[Ticket])
def get_tickets():
    query = "SELECT * FROM Tickets"
    return execute_query(query)

@app.get("/api/tickets/{ticket_id}", response_model=Ticket)
def get_ticket(ticket_id: int):
    query = "SELECT * FROM Tickets WHERE TicketId = %s"
    ticket = execute_query(query, (ticket_id,), fetch_one=True)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@app.post("/api/tickets", response_model=Ticket)
def create_ticket(ticket: TicketCreate):
    query = """
        INSERT INTO Tickets (
            Ticket, 
            Pclass, 
            Fare, 
            Cabin, 
            Embarked
        ) VALUES (%s, %s, %s, %s, %s)
    """
    params = (
        ticket.Ticket,
        ticket.Pclass,
        ticket.Fare,
        ticket.Cabin,
        ticket.Embarked
    )
    execute_query(query, params)
    new_ticket_id = execute_query("SELECT LAST_INSERT_ID() AS TicketId", fetch_one=True)["TicketId"]
    return {**ticket.model_dump(), "TicketId": new_ticket_id}

@app.put("/api/tickets/{ticket_id}", response_model=Ticket)
def update_ticket(ticket_id: int, ticket: TicketCreate):
    query = """
        UPDATE Tickets 
        SET 
            Ticket = %s, 
            Pclass = %s, 
            Fare = %s, 
            Cabin = %s, 
            Embarked = %s 
        WHERE TicketId = %s
    """
    params = (
        ticket.Ticket,
        ticket.Pclass,
        ticket.Fare,
        ticket.Cabin,
        ticket.Embarked,
        ticket_id
    )
    execute_query(query, params)
    return {**ticket.model_dump(), "TicketId": ticket_id}

@app.delete("/api/tickets/{ticket_id}")
def delete_ticket(ticket_id: int):
    query = "DELETE FROM Tickets WHERE TicketId = %s"
    execute_query(query, (ticket_id,))
    return {"message": "Ticket deleted successfully"}

# Survivors CRUD
@app.get("/api/survivors", response_model=List[Survivor])
def get_survivors():
    query = "SELECT * FROM Survivors"
    return execute_query(query)

@app.get("/api/survivors/{survivor_id}", response_model=Survivor)
def get_survivor(survivor_id: int):
    query = "SELECT * FROM Survivors WHERE SurvivorId = %s"
    survivor = execute_query(query, (survivor_id,), fetch_one=True)
    if not survivor:
        raise HTTPException(status_code=404, detail="Survivor not found")
    return survivor

@app.post("/api/survivors", response_model=Survivor)
def create_survivor(survivor: SurvivorCreate):
    query = "INSERT INTO Survivors (PassengerId, Survived) VALUES (%s, %s)"
    params = (survivor.PassengerId, survivor.Survived)
    execute_query(query, params)
    new_survivor_id = execute_query("SELECT LAST_INSERT_ID() AS SurvivorId", fetch_one=True)["SurvivorId"]
    return {**survivor.model_dump(), "SurvivorId": new_survivor_id}

@app.put("/api/survivors/{survivor_id}", response_model=Survivor)
def update_survivor(survivor_id: int, survivor: SurvivorCreate):
    query = "UPDATE Survivors SET PassengerId = %s, Survived = %s WHERE SurvivorId = %s"
    params = (survivor.PassengerId, survivor.Survived, survivor_id)
    execute_query(query, params)
    return {**survivor.model_dump(), "SurvivorId": survivor_id}

@app.delete("/api/survivors/{survivor_id}")
def delete_survivor(survivor_id: int):
    query = "DELETE FROM Survivors WHERE SurvivorId = %s"
    execute_query(query, (survivor_id,))
    return {"message": "Survivor deleted successfully"}

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)