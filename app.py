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
    elif estado == 'Agendar':
        # Aquí pones tu enlace de Calendly real
        return jsonify({
            "mensaje": "¡Genial! Haz clic en el botón de abajo para abrir mi agenda.",
            "opciones": ["Abrir Calendly"] 
        })
    elif estado == 'Abrir Calendly':
        # Esto redirige al usuario o le muestra el link
        return jsonify({
            "mensaje": "Copiando enlace: https://calendly.com/TU-USUARIO",
            "opciones": ["Volver al inicio"]
        })
    elif estado == 'Volver' or estado == 'Volver al inicio':
        return jsonify({
            "mensaje": "¡Hola! Soy el asistente de JyL. ¿En qué te ayudo hoy?",
            "opciones": ["Web", "Automatización"]
        })
    
    return jsonify({
        "mensaje": "No entendí, pero puedes contactarme directamente.",
        "opciones": [] })

if __name__ == "__main__":
    app.run(debug=True)
    