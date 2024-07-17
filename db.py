# db.py
import sqlite3

DATABASE_NAME = "iot.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS admin (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )""",
        """CREATE TABLE IF NOT EXISTS company (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company_name TEXT NOT NULL,
                company_api_key TEXT NOT NULL
            )""",
        """CREATE TABLE IF NOT EXISTS location (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company_id INTEGER NOT NULL,
                location_name TEXT NOT NULL,
                location_country TEXT NOT NULL,
                location_city TEXT NOT NULL,
                location_meta TEXT,
                FOREIGN KEY (company_id) REFERENCES company(id)
            )""",
        """CREATE TABLE IF NOT EXISTS sensor (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                location_id INTEGER NOT NULL,
                sensor_name TEXT NOT NULL,
                sensor_category TEXT,
                sensor_meta TEXT,
                sensor_api_key TEXT NOT NULL,
                FOREIGN KEY (location_id) REFERENCES location(id)
            )""",
        """CREATE TABLE IF NOT EXISTS sensor_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sensor_id INTEGER NOT NULL,
                sensor_data_name TEXT NOT NULL,
                sensor_data_value TEXT NOT NULL,
                timestamp INTEGER NOT NULL,
                FOREIGN KEY (sensor_id) REFERENCES sensor(id)
            )"""
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
    db.commit()
