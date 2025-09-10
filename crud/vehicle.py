from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from models.vehicle import vehicles
from typing import Any
from schemas.vehicle import Vehicle

def get_all(db: Session) -> list[dict[str,Any]]:
    all_vehicles = db.execute(select(vehicles)).mappings().all()
    return [dict(row) for row in all_vehicles]


def get_one(db: Session, id: int) -> dict[str, Any]:
    vehicle = db.execute(select(vehicles).where(vehicles.c.id == id)).mappings().first() 
    if vehicle:
        return dict(vehicle)
    else:
        return {}

def create(db: Session, vehicle: Vehicle) -> dict[str, Any]:
    new_vehicle = {
        "marca": vehicle.brand, 
        "sucursal": vehicle.location,
        "nombre_persona": vehicle.person_name
    }
    result = db.execute(vehicles.insert().values(new_vehicle).returning(vehicles))

    db.commit()
    row = result.fetchone()

    if row:
        return dict(row._mapping)
    else:
        return {}

def update_vehicle(db, id: int, vehicle: Vehicle) -> dict[str, Any]:
    db.execute(
        update(vehicles)
        .values(
            marca=vehicle.brand,
            sucursal=vehicle.location,
            nombre_persona=vehicle.person_name
        )
        .where(vehicles.c.id == id)
    )
    db.commit()
    return get_one(db, id)

def delete_vehicle(db, id: int) -> int:
    result = db.execute(delete(vehicles).where(vehicles.c.id == id))
    db.commit()
    return result.rowcount
