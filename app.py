from flask import Flask, request, jsonify
from flask_cors import CORS
from app.services import analizar_duda_con_ia
from app.db import registrar_interaccion, validar_usuario, obtener_historial

app = Flask(__name__)
CORS(app)  # Permite conexiones desde cualquier web
# ENDPOINT: HOME
@app.route('/', methods=['GET'])
def home():
    return "Home"
# ENDPOINT: LOGIN
@app.route('/api/login', methods=['POST'])
def login():
    datos = request.json
    user_id = datos.get('user_id')
    
    nombre = validar_usuario(user_id)
    if nombre:
        return jsonify({"success": True, "user_id": user_id, "nombre": nombre})
    return jsonify({"success": False, "mensaje": "Usuario no encontrado"}), 404

#  ENDPOINT: CHAT (IA)
@app.route('/api/chat', methods=['POST'])
def chat():
    datos = request.json
    print("📢 RECIBIDO DEL FRONTEND:", datos)
    user_id = datos.get('user_id')
    mensaje = datos.get('mensaje')
    
    if not validar_usuario(user_id):
        return jsonify({"error": "No autorizado"}), 401

    # Procesar con IA
    resultado = analizar_duda_con_ia(mensaje)
    
    # Guardar en BD
    guardado = registrar_interaccion(user_id, mensaje, resultado)
    
    return jsonify({
        "respuesta": resultado["respuesta"],
        "info": {
            "categoria": resultado["categoria"],
            "urgencia": resultado["urgencia"],
            "guardado": guardado
        }
    })

#  ENDPOINT: CONSULTAS (Historial)
@app.route('/api/consultas', methods=['GET'])
def consultas():
    # Leemos los filtros de la URL (Query Params)
    user_id = request.args.get('user_id')
    categoria = request.args.get('categoria')
    
    # Llamamos a la función inteligente de db.py
    resultados = obtener_historial(user_id, categoria)
    
    return jsonify(resultados)

if __name__ == '__main__':
    print("🚀 Servidor CAU escuchando en http://localhost:5000")
    app.run(debug=True, port=5000)