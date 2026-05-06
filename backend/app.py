import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

nama_owner = os.environ.get('NAMA_PRAKTIKAN', 'Naufal Zahid')
nim_owner = os.environ.get('NIM_PRAKTIKAN', '2405787')

katalog_data = {
    "judul_katalog": f"Katalog PC Building {nama_owner}",
    "pemilik": nama_owner,
    "nim": nim_owner,
    "items": [
        "NVIDIA GeForce RTX 4090 24GB",
        "AMD Ryzen 7 7800X3D",
        "Intel Core i9-14900K",
        "Samsung 990 Pro 2TB NVMe",
        "ASUS ROG Maximus Z790 Dark Hero"
    ]
}

@app.route('/api/info', methods=['GET'])
def get_info():
    return jsonify(katalog_data)

@app.route('/api/add-item', methods=['POST'])
def add_item():
    new_item = request.json.get('item')
    if new_item:
        katalog_data["items"].append(new_item)
        return jsonify({"message": "Item berhasil ditambahkan!", "items": katalog_data["items"]}), 201
    return jsonify({"error": "Data tidak valid"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)