from pydantic import BaseModel, Field
from typing import Optional

class Vehicle(BaseModel):
    brand: str = Field(alias="marca")
    location: str = Field(alias="sucursal")
    person_name: str = Field(alias="nombre_persona")

    class Config:
        populate_by_name = True

class VehicleOut(Vehicle):
    id: Optional[int]

