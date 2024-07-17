# controller.py
from db import get_db

# Admin functions
def create_admin(username, password):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO admin (username, password) VALUES (?, ?)"
    cursor.execute(statement, [username, password])
    db.commit()
    return cursor.lastrowid

# Company functions
def create_company(company_name, company_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO company (company_name, company_api_key) VALUES (?, ?)"
    cursor.execute(statement, [company_name, company_api_key])
    db.commit()
    return cursor.lastrowid

def get_company(company_id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM company WHERE id = ?"
    cursor.execute(statement, [company_id])
    return cursor.fetchone()

def get_companies():
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM company"
    cursor.execute(statement)
    return cursor.fetchall()

def update_company(company_id, company_name, company_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE company SET company_name = ?, company_api_key = ? WHERE id = ?"
    cursor.execute(statement, [company_name, company_api_key, company_id])
    db.commit()
    return True

def delete_company(company_id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM company WHERE id = ?"
    cursor.execute(statement, [company_id])
    db.commit()
    return True

# Location functions
def create_location(company_id, location_name, location_country, location_city, location_meta):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO location (company_id, location_name, location_country, location_city, location_meta) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(statement, [company_id, location_name, location_country, location_city, location_meta])
    db.commit()
    return cursor.lastrowid

def get_location(location_id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM location WHERE id = ?"
    cursor.execute(statement, [location_id])
    return cursor.fetchone()

def get_locations():
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM location"
    cursor.execute(statement)
    return cursor.fetchall()

def update_location(location_id, location_name, location_country, location_city, location_meta):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE location SET location_name = ?, location_country = ?, location_city = ?, location_meta = ? WHERE id = ?"
    cursor.execute(statement, [location_name, location_country, location_city, location_meta, location_id])
    db.commit()
    return True

def delete_location(location_id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM location WHERE id = ?"
    cursor.execute(statement, [location_id])
    db.commit()
    return True

# Sensor functions
def create_sensor(location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO sensor (location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(statement, [location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key])
    db.commit()
    return cursor.lastrowid

def get_sensor(sensor_id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM sensor WHERE id = ?"
    cursor.execute(statement, [sensor_id])
    return cursor.fetchone()

def get_sensors():
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM sensor"
    cursor.execute(statement)
    return cursor.fetchall()

def update_sensor(sensor_id, sensor_name, sensor_category, sensor_meta, sensor_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE sensor SET sensor_name = ?, sensor_category = ?, sensor_meta = ?, sensor_api_key = ? WHERE id = ?"
    cursor.execute(statement, [sensor_name, sensor_category, sensor_meta, sensor_api_key, sensor_id])
    db.commit()
    return True

def delete_sensor(sensor_id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM sensor WHERE id = ?"
    cursor.execute(statement, [sensor_id])
    db.commit()
    return True

# Sensor Data functions
def insert_sensor_data(sensor_id, sensor_data_name, sensor_data_value, timestamp):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO sensor_data (sensor_id, sensor_data_name, sensor_data_value, timestamp) VALUES (?, ?, ?, ?)"
    cursor.execute(statement, [sensor_id, sensor_data_name, sensor_data_value, timestamp])
    db.commit()
    return cursor.lastrowid

def get_sensor_data(sensor_id, from_timestamp, to_timestamp):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM sensor_data WHERE sensor_id = ? AND timestamp BETWEEN ? AND ?"
    cursor.execute(statement, [sensor_id, from_timestamp, to_timestamp])
    return cursor.fetchall()
