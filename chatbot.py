import random
import spacy

# Cargar el modelo de spaCy en español
nlp = spacy.load("es_core_news_sm")

# Diccionario de respuestas con más variaciones
respuestas = {
    "saludo": ["¡Hola! ¿Cómo te sientes hoy?", "¡Hola! ¿En qué puedo ayudarte?", "¡Bienvenido! ¿Cómo estás?"],
    "tristeza": ["Lamento que te sientas así. ¿Quieres hablar sobre ello?", 
                 "Recuerda que no estás solo. Hablar con alguien de confianza puede ayudar.",
                 "Los momentos difíciles pasan. ¿Quieres contarme qué sucede?"],
    "ansiedad": ["La respiración profunda puede ayudar a calmar la ansiedad. ¿Quieres intentar una técnica?", 
                 "Si te sientes ansioso con frecuencia, puede ser útil escribir tus pensamientos.",
                 "Escuchar música relajante puede ayudar a reducir la ansiedad. ¿Te gustaría probarlo?"],
    "felicidad": ["¡Me alegra escuchar eso! ¿Qué ha hecho que tu día sea bueno?", 
                  "La felicidad es contagiosa. ¡Sigue disfrutando tu día!",
                  "¡Eso es genial! Aprecia cada momento de felicidad."],
    "despedida": ["Hasta luego. ¡Cuídate!", "Adiós, espero hablar contigo pronto.", "Nos vemos, cuídate mucho 😊"]
}

# Función para clasificar la intención del usuario
def clasificar_intencion(mensaje):
    doc = nlp(mensaje.lower())  # Procesar el texto con spaCy
    for token in doc:
        if token.lemma_ in ["hola", "buenos", "saludo"]:
            return "saludo"
        elif token.lemma_ in ["triste", "deprimido", "llorar"]:
            return "tristeza"
        elif token.lemma_ in ["ansiedad", "estresado", "nervioso"]:
            return "ansiedad"
        elif token.lemma_ in ["feliz", "contento", "alegre"]:
            return "felicidad"
        elif token.lemma_ in ["adios", "hasta", "despedida"]:
            return "despedida"
    
    return "desconocido"

# Función para obtener la respuesta del chatbot
def obtener_respuesta(mensaje):
    intencion = clasificar_intencion(mensaje)
    if intencion in respuestas:
        return random.choice(respuestas[intencion])
    
    return "Lo siento, no entiendo bien. ¿Puedes explicarlo de otra manera?"

# Bucle principal del chatbot
def iniciar_chat():
    print("🤖 Chatbot de Bienestar (con NLP): Escribe 'adios' para salir.")
    while True:
        mensaje_usuario = input("Tú: ")
        if mensaje_usuario.lower() in ["adios", "hasta luego", "nos vemos"]:
            print("Chatbot: Hasta luego. ¡Cuídate! 😊")
            break
        respuesta = obtener_respuesta(mensaje_usuario)
        print(f"Chatbot: {respuesta}")

# Ejecutar el chatbot
if __name__ == "__main__":
    iniciar_chat() 