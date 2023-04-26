from fastapi import FastAPI, HTTPException
from my_database import MyDatabase

app = FastAPI(title="Shehryar Ke Bikes")
db = MyDatabase()


@app.get("/")
def home():
    return {"message": "Welcome to Shehryar ki Dukaan!!"}


@app.get("/Select_Bike")
def select_bike(id: int):
    bike = db.select_bike(id)
    if bike:
        return bike
    else:
        return f"Bike: {id} does not exist!"


@app.get("/All_Bikes")
def get_all_bikes():
    return db.get_all_bikes()


@app.post("/Insert_bike")
def insert_bike(id: int, name: str, cc: int, color: str, price: int):
    result = db.insert_bike(id, name, cc, color, price)
    if bike in result:
        return f"bike:{name} created successfully."
    else:
        return f"{name} Not Created."


@app.post("/Insert_many_bikes")
def insert_many_bike(bikes: list[dict]):
    result = db.insert_many_bike([bike for bike in bikes])
    if bike1 in result:
        return {"message": "Bikes created successfully."}
    else:
        return f"Bikes not created."


@app.put("/Update_bike")
def update_bike(id: int, price: int):
    result = db.update_bike(id, price)
    if bike in result:
        return f"{id} updated successfully."
    else:
        return f"{id} not deleted."


@app.put("/Update_many_bikes")
def update_many_bikes(bikes: list[dict]):
    result = db.update_many_bikes([bike for bike in bikes])
    if bike1 in result:
        return "Bikes updated successfully."
    else:
        return "Bikes not updated."


@app.delete("/Delete_bike")
def delete_bike(id: int):
    result = db.delete_bike(id)
    if bike in result:
        return f"{id} deleted successfully."
    else:
        return f"{id} not deleted"


@app.delete("/Delete_many_bikes")
def delete_many_bikes(bikes: list[int]):
    result = db.delete_many_bikes(bikes)
    if bike in result:
        return "Bikes deleted successfully."
    else:
        return "Bikes not deleted."
