import random
import re  # Librería para trabajar con expresiones regulares

# Diccionario de respuestas con más variaciones
respuestas = {
    "hola": ["¡Hola! ¿Cómo te sientes hoy?", "¡Hola! ¿En qué puedo ayudarte?", "¡Bienvenido! ¿Cómo estás?"],
    "triste": ["Lamento que te sientas así. ¿Quieres hablar sobre ello?", 
               "Recuerda que no estás solo. Hablar con alguien de confianza puede ayudar.",
               "Los momentos difíciles pasan. ¿Quieres contarme qué sucede?"],
    "deprimido": ["Cuando te sientas así, intenta hablar con alguien en quien confíes.", 
                  "A veces escribir sobre lo que sientes puede ayudar."],
    "ansioso": ["La respiración profunda puede ayudar a calmar la ansiedad. ¿Quieres intentar una técnica?", 
                "Si te sientes ansioso con frecuencia, puede ser útil escribir tus pensamientos.",
                "Escuchar música relajante puede ayudar a reducir la ansiedad. ¿Te gustaría probarlo?"],
    "estresado": ["El estrés es normal, pero recuerda tomarte un descanso.", 
                  "La meditación o el ejercicio pueden ayudar a reducir el estrés."],
    "feliz": ["¡Me alegra escuchar eso! ¿Qué ha hecho que tu día sea bueno?", 
              "La felicidad es contagiosa. ¡Sigue disfrutando tu día!",
              "¡Eso es genial! Aprecia cada momento de felicidad."],
    "cansado": ["El descanso es importante. ¿Has dormido bien últimamente?", 
                "Si te sientes cansado, intenta relajarte un poco."],
    "gracias": ["¡De nada! Estoy aquí para ayudarte.", "¡Siempre un placer ayudarte!", "Me alegra ser útil 😊"],
    "adios": ["Hasta luego. ¡Cuídate!", "Adiós, espero hablar contigo pronto.", "Nos vemos, cuídate mucho 😊"]
}

# Diccionario para detectar preguntas específicas
preguntas = {
    "como puedo ser feliz": ["La felicidad depende de muchas cosas. ¿Qué cosas te hacen sentir bien?",
                             "Cada persona encuentra la felicidad de manera diferente. ¿Qué te gusta hacer?"],
    "que hacer si estoy triste": ["Puedes hablar con alguien en quien confíes o hacer algo que disfrutes.",
                                  "A veces, salir a caminar o escribir sobre lo que sientes puede ayudar."],
    "como manejo la ansiedad": ["La respiración profunda y la meditación pueden ser útiles.",
                                "Intentar enfocarte en el presente puede ayudar a reducir la ansiedad."]
}

# Función para obtener respuesta del chatbot
def obtener_respuesta(mensaje):
    mensaje = mensaje.lower().strip()  # Convertir a minúsculas y quitar espacios extra
    
    # Buscar coincidencia exacta con preguntas frecuentes
    for pregunta, respuestas_posibles in preguntas.items():
        if pregunta in mensaje:
            return random.choice(respuestas_posibles)
    
    # Buscar palabras clave dentro del mensaje
    for clave, respuestas_posibles in respuestas.items():
        if re.search(r'\b' + clave + r'\b', mensaje):  # Usa regex para evitar coincidencias parciales
            return random.choice(respuestas_posibles)
    
    return "Lo siento, no entiendo. ¿Puedes reformular tu pregunta?"

# Bucle principal del chatbot
def iniciar_chat():
    print("🤖 Chatbot de Bienestar: Escribe 'adios' para salir.")
    while True:
        mensaje_usuario = input("Tú: ")
        if mensaje_usuario.lower() == "adios":
            print("Chatbot: Hasta luego. ¡Cuídate! 😊")
            break
        respuesta = obtener_respuesta(mensaje_usuario)
        print(f"Chatbot: {respuesta}")

# Ejecutar el chatbot
if __name__ == "__main__":
    iniciar_chat()