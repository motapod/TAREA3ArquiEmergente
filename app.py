# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import controller
from db import create_tables

app = Flask(__name__)
CORS(app)

# Company endpoints
@app.route('/api/v1/companies', methods=["GET"])
def get_companies():
    companies = controller.get_companies()
    return jsonify(companies)

@app.route('/api/v1/company', methods=["POST"])
def create_company():
    data = request.get_json()
    company_name = data['company_name']
    company_api_key = data['company_api_key']
    company_id = controller.create_company(company_name, company_api_key)
    return jsonify({'company_id': company_id}), 201

@app.route('/api/v1/company/<int:company_id>', methods=["GET"])
def get_company(company_id):
    company = controller.get_company(company_id)
    return jsonify(company)

@app.route('/api/v1/company/<int:company_id>', methods=["PUT"])
def update_company(company_id):
    data = request.get_json()
    company_name = data['company_name']
    company_api_key = data['company_api_key']
    success = controller.update_company(company_id, company_name, company_api_key)
    return jsonify({'success': success})

@app.route('/api/v1/company/<int:company_id>', methods=["DELETE"])
def delete_company(company_id):
    success = controller.delete_company(company_id)
    return jsonify({'success': success})

# Location endpoints
@app.route('/api/v1/locations', methods=["GET"])
def get_locations():
    locations = controller.get_locations()
    return jsonify(locations)

@app.route('/api/v1/location', methods=["POST"])
def create_location():
    data = request.get_json()
    company_id = data['company_id']
    location_name = data['location_name']
    location_country = data['location_country']
    location_city = data['location_city']
    location_meta = data.get('location_meta', '')
    location_id = controller.create_location(company_id, location_name, location_country, location_city, location_meta)
    return jsonify({'location_id': location_id}), 201

@app.route('/api/v1/location/<int:location_id>', methods=["GET"])
def get_location(location_id):
    location = controller.get_location(location_id)
    return jsonify(location)

@app.route('/api/v1/location/<int:location_id>', methods=["PUT"])
def update_location(location_id):
    data = request.get_json()
    location_name = data['location_name']
    location_country = data['location_country']
    location_city = data['location_city']
    location_meta = data.get('location_meta', '')
    success = controller.update_location(location_id, location_name, location_country, location_city, location_meta)
    return jsonify({'success': success})

@app.route('/api/v1/location/<int:location_id>', methods=["DELETE"])
def delete_location(location_id):
    success = controller.delete_location(location_id)
    return jsonify({'success': success})

# Sensor endpoints
@app.route('/api/v1/sensors', methods=["GET"])
def get_sensors():
    sensors = controller.get_sensors()
    return jsonify(sensors)

@app.route('/api/v1/sensor', methods=["POST"])
def create_sensor():
    data = request.get_json()
    location_id = data['location_id']
    sensor_name = data['sensor_name']
    sensor_category = data.get('sensor_category', '')
    sensor_meta = data.get('sensor_meta', '')
    sensor_api_key = data['sensor_api_key']
    sensor_id = controller.create_sensor(location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key)
    return jsonify({'sensor_id': sensor_id}), 201

@app.route('/api/v1/sensor/<int:sensor_id>', methods=["GET"])
def get_sensor(sensor_id):
    sensor = controller.get_sensor(sensor_id)
    return jsonify(sensor)

@app.route('/api/v1/sensor/<int:sensor_id>', methods=["PUT"])
def update_sensor(sensor_id):
    data = request.get_json()
    sensor_name = data['sensor_name']
    sensor_category = data.get('sensor_category', '')
    sensor_meta = data.get('sensor_meta', '')
    sensor_api_key = data['sensor_api_key']
    success = controller.update_sensor(sensor_id, sensor_name, sensor_category, sensor_meta, sensor_api_key)
    return jsonify({'success': success})

@app.route('/api/v1/sensor/<int:sensor_id>', methods=["DELETE"])
def delete_sensor(sensor_id):
    success = controller.delete_sensor(sensor_id)
    return jsonify({'success': success})

# Function to validate sensor API key
def validate_sensor_api_key(api_key):
    sensor = controller.get_sensor_by_api_key(api_key)
    if not sensor:
        abort(400, 'Invalid sensor API key')

# Sensor Data Insertion
@app.route('/api/v1/sensor_data', methods=["POST"])
def insert_sensor_data():
    data = request.get_json()
    sensor_api_key = data.get('api_key', '')
    json_data = data.get('json_data', [])

    # Validate sensor API key
    validate_sensor_api_key(sensor_api_key)
    
    success = True
    for record in json_data:
        try:
            sensor_id = record['sensor_id']  # Assuming sensor_id is part of json_data
            sensor_data_name = record['sensor_data_name']
            sensor_data_value = record['sensor_data_value']
            timestamp = record['timestamp']
            controller.insert_sensor_data(sensor_id, sensor_data_name, sensor_data_value, timestamp)
        except Exception as e:
            success = False
            print(e)
    
    if success:
        return jsonify({'message': 'Sensor data inserted successfully'}), 201
    else:
        return jsonify({'error': 'Failed to insert sensor data'}), 500
if __name__ == '__main__':
    create_tables()
    app.run(host='0.0.0.0', port=80, debug=False)
