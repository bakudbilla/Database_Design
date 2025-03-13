from sqlalchemy.orm import Session
from api.models import Passenger, Ticket, Survivor
import schemas

from sqlalchemy.orm import Session
from api.models import Passenger
import schemas

#CRUD for Passengers
def create_passenger(db: Session, passenger: schemas.PassengerCreate):
    new_passenger = Passenger(
        Name=passenger.Name,
        Sex=passenger.Sex,
        Age=passenger.Age,
        SibSp=passenger.SibSp,
        Parch=passenger.Parch
    )
    db.add(new_passenger)
    db.commit()
    db.refresh(new_passenger)
    return new_passenger

def get_passengers(db: Session):
    return db.query(Passenger).all()

def get_passenger(db: Session, passenger_id: int):
    return db.query(Passenger).filter(Passenger.PassengerId == passenger_id).first()

def update_passenger(db: Session, passenger_id: int, passenger: schemas.PassengerCreate):
    db_passenger = db.query(Passenger).filter(Passenger.PassengerId == passenger_id).first()
    if db_passenger:
        for key, value in passenger.model_dump().items():
            setattr(db_passenger, key, value)
        db.commit()
        db.refresh(db_passenger)
    return db_passenger

def delete_passenger(db: Session, passenger_id: int):
    db_passenger = db.query(Passenger).filter(Passenger.PassengerId == passenger_id).first()
    if db_passenger:
        db.delete(db_passenger)
        db.commit()
    return db_passenger

# CRUD for Tickets
def create_ticket(db: Session, ticket: schemas.TicketCreate):
    new_ticket = Ticket(**ticket.model_dump())
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

def get_tickets(db: Session):
    return db.query(Ticket).all()

def get_ticket(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.TicketId == ticket_id).first()

def update_ticket(db: Session, ticket_id: int, ticket: schemas.TicketCreate):
    db_ticket = db.query(Ticket).filter(Ticket.TicketId == ticket_id).first()
    if db_ticket:
        for key, value in ticket.model_dump().items():
            setattr(db_ticket, key, value)
        db.commit()
        db.refresh(db_ticket)
    return db_ticket

def delete_ticket(db: Session, ticket_id: int):
    db_ticket = db.query(Ticket).filter(Ticket.TicketId == ticket_id).first()
    if db_ticket:
        db.delete(db_ticket)
        db.commit()
    return db_ticket

#  CRUD for Survivors
def create_survivor(db: Session, survivor: schemas.SurvivorCreate):
    new_survivor = Survivor(**survivor.dict())
    db.add(new_survivor)
    db.commit()
    db.refresh(new_survivor)
    return new_survivor

def get_survivors(db: Session):
    return db.query(Survivor).all()

def get_survivor(db: Session, survivor_id: int):
    return db.query(Survivor).filter(Survivor.SurvivorId == survivor_id).first()

def update_survivor(db: Session, survivor_id: int, survivor: schemas.SurvivorCreate):
    db_survivor = db.query(Survivor).filter(Survivor.SurvivorId == survivor_id).first()
    if db_survivor:
        for key, value in survivor.dict().items():
            setattr(db_survivor, key, value)
        db.commit()
        db.refresh(db_survivor)
    return db_survivor

def delete_survivor(db: Session, survivor_id: int):
    db_survivor = db.query(Survivor).filter(Survivor.SurvivorId == survivor_id).first()
    if db_survivor:
        db.delete(db_survivor)
        db.commit()
    return db_survivor
