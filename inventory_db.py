import sqlite3
from datetime import datetime

class InventoryDB:
    def __init__(self, db_path="inventory.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        try:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS products(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            self.conn.commit()
            return True
        except Exception as e:
            return e
    
    def add_item(self, name, quantity):
        self.cursor.execute(
            """
            INSERT INTO products(name, quantity)
            VALUES(?, ?)
            """, (name, quantity)
        )
        self.conn.commit()
        return self.cursor.lastrowid
    
    def get_all_items(self):
        self.cursor.execute(
            """
            SELECT * FROM products
            """
        )
        return self.cursor.fetchall()
    
    def close(self):
        self.conn.close()
