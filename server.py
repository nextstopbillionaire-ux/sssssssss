from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import json
import os

app = Flask(__name__, static_folder='.')
CORS(app)

QUICKLINKS_FILE = 'quicklinks.txt'
RESOURCES_FILE = 'resources.txt'

def read_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            try:
                return json.load(f)
            except:
                return []
    return []

def write_file(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

@app.route('/api/quicklinks', methods=['GET'])
def get_quicklinks():
    data = read_file(QUICKLINKS_FILE)
    return jsonify(data)

@app.route('/api/quicklinks', methods=['POST'])
def save_quicklinks():
    data = request.json
    write_file(QUICKLINKS_FILE, data)
    return jsonify({'status': 'success'})

@app.route('/api/resources', methods=['GET'])
def get_resources():
    data = read_file(RESOURCES_FILE)
    return jsonify(data)

@app.route('/api/resources', methods=['POST'])
def save_resources():
    data = request.json
    write_file(RESOURCES_FILE, data)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
