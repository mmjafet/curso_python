from flask import Flask, jsonify, request

app = Flask(__name__)

# Almacenamiento en memoria
usuarios = []

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios)

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    nuevo_usuario = request.get_json()
    usuarios.append(nuevo_usuario)
    return jsonify(nuevo_usuario), 201

if __name__ == '__main__':
    app.run(debug=True)
