from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from pydantic_core import core_schema

# Helper function to handle MongoDB ObjectId
class PyObjectId(str):
    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        json_schema = handler(core_schema)
        json_schema.update(type="string", format="objectid")
        return json_schema

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, handler):
        return core_schema.no_info_after_validator_function(
            cls.validate,
            core_schema.str_schema(),
            serialization=core_schema.to_string_ser_schema(),
        )

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return str(v)

# Base model for MongoDB documents
class MongoDBBaseModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True

# Passenger model
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

class PassengerDB(PassengerBase, MongoDBBaseModel):
    class Config:
        json_encoders = {ObjectId: str}  # Ensure ObjectId is serialized as a string

# Ticket model
class TicketBase(BaseModel):
    TicketId: int
    PassengerId: int
    Fare: float
    Cabin: Optional[str] = None
    Embarked: Optional[str] = None

class TicketCreate(TicketBase):
    pass

class TicketDB(TicketBase, MongoDBBaseModel):
    class Config:
        json_encoders = {ObjectId: str}  # Ensure ObjectId is serialized as a string

# Survivor model
class SurvivorBase(BaseModel):
    SurvivorId: int
    PassengerId: int
    Survived: bool

class SurvivorCreate(SurvivorBase):
    pass

class SurvivorDB(SurvivorBase, MongoDBBaseModel):
    class Config:
        json_encoders = {ObjectId: str}  