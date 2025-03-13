from pydantic import BaseModel
from typing import Optional

# Passenger Schema
class PassengerBase(BaseModel):
    Name: str
    Sex: str
    Age: Optional[float]
    SibSp: int
    Parch: int

class PassengerCreate(PassengerBase):
    pass

class PassengerResponse(PassengerBase):
    passenger_id: int

    class Config:
        orm_mode = True

#
class TicketBase(BaseModel):
    Ticket: str
    Pclass: int
    Fare: float
    Cabin: Optional[str]
    Embarked: Optional[str]

class TicketCreate(TicketBase):
    pass

class TicketResponse(TicketBase):
    TicketId: int

    class Config:
        orm_mode = True

#  Survivor Schema
class SurvivorBase(BaseModel):
    PassengerId: int
    Survived: bool

class SurvivorCreate(SurvivorBase):
    pass

class SurvivorResponse(BaseModel):
    PassengerId: int  # No SurvivorId
    Survived: bool

    class Config:
        orm_mode = True

