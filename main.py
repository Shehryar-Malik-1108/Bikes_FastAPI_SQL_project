from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from my_database import MyDatabase


app = FastAPI(title="Shehryar Ke Bikes")
db = MyDatabase()


@app.get("/")
def home():
    return {"message": "Welcome to Shehryar ki Dukaan!!"}


@app.get("/Select_Bike")
def select_bike(id: int):
    bike = db.select_bike(id)
    if "message" in bike:
        raise HTTPException(status_code=404, detail=bike["message"])
    return bike


@app.get("/All_Bikes")
def get_all_bikes():
    return db.get_all_bikes()


@app.post("/Insert_bike")
def insert_bike(id: int, name: str, cc: int, color: str, price: int):
    result = db.insert_bike(id, name, cc, color, price)
    if "message" in result:
        raise HTTPException(status_code=400, detail=result["message"])
    return {"message": "Bike created successfully."}


@app.post("/Insert_many_bikes")
def insert_many_bike(bikes: list[dict]):
    result = db.insert_many_bike([bike for bike in bikes])
    if "message" in result:
        raise HTTPException(status_code=400, detail=result["message"])
    return {"message": "Bikes created successfully."}


@app.put("/Update_bike")
def update_bike(id: int, price: int):
    result = db.update_bike(id, price)
    if "message" in result:
        raise HTTPException(status_code=404, detail=result["message"])
    return {"message": "Bike updated successfully."}


@app.put("/Update_many_bikes")
def update_many_bikes(bikes: list[dict]):
    result = db.update_many_bikes([bike for bike in bikes])
    if "message" in result:
        raise HTTPException(status_code=404, detail=result["message"])
    return {"message": "Bikes updated successfully."}


@app.delete("/Delete_bike")
def delete_bike(id: int):
    result = db.delete_bike(id)
    if "message" in result:
        raise HTTPException(status_code=404, detail=result["message"])
    return {"message": "Bike deleted successfully."}


@app.delete("/Delete_many_bikes")
def delete_many_bikes(bikes: list[int]):
    result = db.delete_many_bikes(bikes)
    if "message" in result:
        raise HTTPException(status_code=404, detail=result["message"])
    return {"message": "Bikes deleted successfully."}
