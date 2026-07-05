from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Esta es tu ruta actual (¡no la borres!)
@app.route("/")
def home():
    return render_template("index.html")

# Aquí pegamos la nueva ruta del bot
@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    estado = data.get('estado', 'inicio')
    
    if estado == 'inicio':
        return jsonify({
            "mensaje": "¡Hola! Soy el asistente de JyL. ¿En qué te ayudo hoy?",
            "opciones": ["Web", "Automatización"]
        })
    elif estado == 'Web':
        return jsonify({
            "mensaje": "Desarrollo sitios web modernos. ¿Quieres agendar una consulta?",
            "opciones": ["Agendar", "Volver"]
        })
    elif estado == 'Automatización':
        return jsonify({
            "mensaje": "Automatizo procesos para que ahorres tiempo. ¿Te interesa?",
            "opciones": ["Agendar", "Volver"]
        })
    
   # ... (tus elif anteriores)
    
    # Asegúrate de que incluso en el caso de error se envíe una lista vacía de opciones
    return jsonify({
        "mensaje": "No entendí, pero puedes contactarme directamente.",
        "opciones": [] 
    })

if __name__ == "__main__":
    app.run(debug=True)