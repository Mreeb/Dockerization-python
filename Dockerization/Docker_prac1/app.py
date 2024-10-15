from flask import Flask, jsonify, request
import os
import json
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
app.logger.setLevel(logging.INFO)



@app.route('/get_json_data', methods=["POST"])
def get_json_data():
    path = request.form.get("path")
    name = request.form.get("name")
    
    # Path to the directory and JSON file
    json_file_path = os.path.join('dir', f'{path}.json')

    try:
        # Read the JSON file
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        
        # Include the name in the response
        response = {
            "name": name,
            "data": data
        }
        return jsonify(response), 200
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding JSON"}), 400
