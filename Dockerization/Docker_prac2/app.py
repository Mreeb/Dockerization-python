from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# POST method to upload a JSON file using form-data
@app.route('/upload', methods=['POST'])
def upload_json():
    try:
        # Get the user_id from form-data
        user_id = request.form.get('user_id')
        if not user_id:
            return jsonify({"error": "User ID is required"}), 400
        
        # Get the file from form-data
        file = request.files.get('file')
        if not file or not file.filename.endswith('.json'):
            return jsonify({"error": "A .json file is required"}), 400

        file_path = os.path.join(UPLOAD_FOLDER, f'{user_id}.json')

        # Save the file with the user_id as filename
        file.save(file_path)

        return jsonify({"message": f"File saved as {user_id}.json"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET method to retrieve JSON files by user_id
@app.route('/getfile/<user_id>', methods=['GET'])
def get_json(user_id):
    file_path = os.path.join(UPLOAD_FOLDER, f'{user_id}.json')

    if os.path.exists(file_path):
        return send_file(file_path, mimetype='application/json')

    return jsonify({"error": "File not found"}), 404

# if __name__ == '__main__':
#     app.run(debug=True, port=5000, host="0.0.0.0")
