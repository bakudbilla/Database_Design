# models.py
from pydantic import BaseModel
from typing import Optional

class PassengerBase(BaseModel):
    PassengerId: int
    Name: str
    Sex: str
    Age: float
    SibSp: int
    Parch: int
    TicketId: Optional[int] = None

class PassengerCreate(PassengerBase):
    pass

class Passenger(PassengerBase):
    class Config:
        from_attributes = True

class TicketBase(BaseModel):
    TicketId: int
    Ticket: str
    Pclass: int
    Fare: float
    Cabin: Optional[str] = None
    Embarked: Optional[str] = None

class TicketCreate(TicketBase):
    pass

class Ticket(TicketBase):
    class Config:
        from_attributes = True

class SurvivorBase(BaseModel):
    SurvivorId: int
    PassengerId: int
    Survived: bool

class SurvivorCreate(SurvivorBase):
    pass

class Survivor(SurvivorBase):
    class Config:
        from_attributes = True