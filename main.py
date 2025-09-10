from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from routes.vehicle import vehicle_router
from routes.auth import auth_router

app = FastAPI(
    title="API Vehiculos",
    description="Esta api con fastAPI muestra un crud de las marcas de vehiculos, ubicación y nombre de persona",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "vehicles",
            "description": "vehicles routes"
        }
    ],
)

@app.get("/")
def read_root():
    return {"msg": "Hello 🚀"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      
    allow_credentials=True,     
    allow_methods=["*"],        
    allow_headers=["*"],        
)

app.include_router(vehicle_router)
app.include_router(auth_router)