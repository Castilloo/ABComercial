from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from crud.vehicle import update_vehicle, get_all, get_one, delete_vehicle, create
from schemas.vehicle import Vehicle, VehicleOut
from config.db import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from utils.auth import decode_access_token
from fastapi import Security


vehicle_router = APIRouter(tags=["vehicles"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Token inválido")
    return payload["sub"]



@vehicle_router.get("/vehicles", response_model=list[VehicleOut])
def read_vehicles(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return get_all(db)

@vehicle_router.post("/vehicles", response_model=VehicleOut)
def create_vehicle(vehicle: Vehicle, db:Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return create(db, vehicle)

@vehicle_router.get("/vehicles/{id}", response_model=VehicleOut)
def get_vehicle(id: int, db:Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    vehicle = get_one(db, id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Dato no encontrado")
    return vehicle

@vehicle_router.put("/vehicles/{id}", response_model=VehicleOut)
def update_existing_vehicle(id: int, vehicle: Vehicle, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return update_vehicle(db, id, vehicle)

@vehicle_router.delete("/vehicles/{id}", status_code=204)
def delete_existing_vehicle(id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    deleted = delete_vehicle(db, id)
    if deleted == 0: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vehículo con id {id} no encontrado"
        )