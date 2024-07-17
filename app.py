# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import controller
from db import create_tables

app = Flask(__name__)
CORS(app)

@app.before_first_request
def initialize():
    create_tables()

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

# Similar endpoints for Location, Sensor, Sensor Data...

# Sensor Data Insertion
@app.route('/api/v1/sensor_data', methods=["POST"])
def insert_sensor_data():
    data = request.get_json()
    sensor_api_key = data['api_key']
    json_data = data['json_data']
    
    sensor = controller.get_sensor_by_api_key(sensor_api_key)
    if sensor is None:
        return jsonify({'error': 'Invalid sensor API key'}), 400
    
    sensor_id = sensor['id']
    success = True
    for record in json_data:
        try:
            controller.insert_sensor_data(sensor_id, record['sensor_data_name'], record['sensor_data_value'], record['timestamp'])
        except Exception as e:
            success = False
            print(e)
    return jsonify({'success': success})

if __name__ == '__main__':
    create_tables()
    app.run(host='0.0.0.0', port=80, debug=False)  # Cambia el puerto a 80
