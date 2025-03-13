from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
<<<<<<< HEAD
from api.database import Base
=======
from .database import Base  
>>>>>>> 90d4114aa4d9e74f6928c27e69d8e3bd1bff27b5

class Passenger(Base):
    __tablename__ = "passengers"

    PassengerId = Column(Integer, primary_key=True, index=True)
    Name = Column(String(255), nullable=False)
    Sex = Column(String(10), nullable=False)
    Age = Column(Float, nullable=True)
    SibSp = Column(Integer, nullable=True)
    Parch = Column(Integer, nullable=True)

    # One-to-Many relationship (One Passenger -> Many Tickets)
    tickets = relationship("Ticket", back_populates="passenger")

    # One-to-One relationship with Survivor
    survivor = relationship("Survivor", back_populates="passenger", uselist=False)


class Ticket(Base):
    __tablename__ = "tickets"

    TicketId = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Ticket = Column(String(50), unique=True, nullable=False)
    Pclass = Column(Integer, nullable=False)
    Fare = Column(Float, nullable=False)
    Cabin = Column(String(50), nullable=True)
    Embarked = Column(String(1), nullable=True)

    # Foreign Key (Every Ticket belongs to one Passenger)
    passenger_id = Column(Integer, ForeignKey("passengers.PassengerId"))
    
    # Relationship back to Passenger
    passenger = relationship("Passenger", back_populates="tickets")


class Survivor(Base):
    __tablename__ = "survivors"

    PassengerId = Column(Integer, ForeignKey("passengers.PassengerId"), primary_key=True)
    Survived = Column(Boolean, nullable=False)

    # Relationship back to Passenger
    passenger = relationship("Passenger", back_populates="survivor")
