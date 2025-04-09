import os, json, utils
from flask import request, jsonify
from datetime import datetime


def guardar_json():
    if not request.is_json:
        return jsonify({"error": "Se requiere un archivo JSON"}), 400

    data = request.get_json()
    ruta = request.path.strip("/")
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = os.path.join(utils.crear_carpeta(ruta), f"{current_time}.json")

    try:
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        return jsonify({"message": f"Archivo guardado como {current_time}.json"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
