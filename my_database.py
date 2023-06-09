import sqlite3


class MyDatabase:
    def __init__(self):
        self.connection = self.get_connection()
        self.create_table()

    def get_connection(self):
        connection = sqlite3.connect("my_database.db", check_same_thread=False)
        return connection

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS bikes (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            cc INTEGER NOT NULL,
            color TEXT NOT NULL,
            price INTEGER NOT NULL
        );""")
        self.connection.commit()

    def select_bike(self, id: int):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM bikes WHERE id=?", (id,))
        bike = cursor.fetchone()
        if bike:
            return {
                "id": bike[0],
                "name": bike[1],
                "cc": bike[2],
                "color": bike[3],
                "price": bike[4]
            }
        else:
            return None

    def get_all_bikes(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM bikes")
        bikes = []
        for bike in cursor.fetchall():
            bikes.append({
                "id": bike[0],
                "name": bike[1],
                "cc": bike[2],
                "color": bike[3],
                "price": bike[4]
            })
        return {"bikes": bikes}

    def insert_bike(self, id: int, name: str, cc: int, color: str, price: int):
        cursor = self.connection.cursor()
        try:
            cursor.execute("INSERT INTO bikes (id, name, cc, color, price) VALUES (?, ?, ?, ?, ?)",
                           (id, name, cc, color, price))
            self.connection.commit()
            return {"message": f"Bike {name} created successfully"}
        except Exception as e:
            return f"Error occurred while creating new bike due to: {e}"

    def insert_many_bike(self, bikes: list[dict]):
        cursor = self.connection.cursor()
        cursor.executemany("INSERT INTO bikes (id, name, cc, color, price) VALUES (?, ?, ?, ?, ?)",
                           [(bike["id"], bike["name"], bike["cc"], bike["color"], bike["price"]) for bike in bikes])
        self.connection.commit()
        if bike1:
            return f"{len(bikes)} bikes created"
        else:
            return "Bikes not created."

    def update_bike(self, id: int, price: int):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE bikes SET price=? WHERE id=?", (price, id))
        self.connection.commit()
        if cursor.rowcount == 1:
            return f"{id} updated."
        else:
            return f"Error occurred while updating {id}."

    def update_many_bikes(self, bikes: list[dict]):
        cursor = self.connection.cursor()
        for bike in bikes:
            cursor.execute(f"UPDATE bikes SET name="f"price='{bike['price']}' WHERE id='{bike['id']}'")
        self.connection.commit()
        if cursor.rowcount > 0:
            return f"{cursor.rowcount} bike(s) updated."
        else:
            return "No bikes updated."

    def delete_bike(self, id: int):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM bikes WHERE id={id}")
        self.connection.commit()
        if cursor.rowcount == 1:
            return f"{id} deleted."
        else:
            return "Error occurred while deleting bike."

    def delete_many_bikes(self, bikes: list[int]):
        cursor = self.connection.cursor()
        id_list = ",".join(str(bike) for bike in bikes)
        cursor.execute(f"DELETE FROM bikes WHERE id IN ({id_list})")
        self.connection.commit()
        if cursor.rowcount > 0:
            return f"{cursor.rowcount} bike(s) deleted."
        return "Bikes not deleted."


if __name__ == "__main__":
    pass
