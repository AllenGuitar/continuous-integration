# Programa que valida las respuestas de 4 preguntas curiosas sobre los michis :)

PREGUNCAT = {
    1: {
        "enunciado": "¿Qué significa FRAP en los gatos?",
        "respuesta": "frenetic random activity period"
    },
    2: {
        "enunciado": "¿Cuántas horas al día duermen los gatos en promedio?",
        "respuesta": "16"
    },
    3: {
        "enunciado": "¿Cómo se llama el órgano extra que tienen los gatos para detectar olores?",
        "respuesta": "organo de jacobson"
    },
    4: {
        "enunciado": "¿Cual es la maxima velocidad (Km/h) que puede alcanzar un gato domestico?",
        "respuesta": "48"
    }
}

def obtener_pregunta(pregunta_id):
    return PREGUNCAT.get(pregunta_id)

def verificar_respuesta(pregunta_id, respuesta_usuario):
    pregunta = obtener_pregunta(pregunta_id)
    if not pregunta:
        return False
    return respuesta_usuario.lower().strip() == pregunta["respuesta"]

def calcular_puntaje(respuestas: dict):
    puntaje = 0
    for pregunta_id, respuesta in respuestas.items():
        if verificar_respuesta(pregunta_id, respuesta):
            puntaje += 1
    return puntaje

def nivel_michi(puntaje):
    if puntaje == 4:
        return "Experto en michis"
    elif puntaje == 3:
        return "Buen conocedor de michis"
    elif puntaje == 2:
        return "Aprendiz"
    else:
        return "Necesitas pasar más tiempo con michis :("

#Validacion de testeos en base al programa

from quiz_gatitos import verificar_respuesta, calcular_puntaje, nivel_michi, obtener_pregunta

def test_frap_correcto():
    assert verificar_respuesta(1, "frenetic random activity period") == True

def test_frap_incorrecto():
    assert verificar_respuesta(1, "free running animal period") == False

def test_ignora_mayusculas():
    assert verificar_respuesta(1, "Frenetic Random Activity Period") == True

def test_puntaje_perfecto():
    respuestas = {
        1: "frenetic random activity period",
        2: "16",
        3: "organo de jacobson",
        4: "48"
    }
    assert calcular_puntaje(respuestas) == 4

def test_puntaje_parcial():
    respuestas = {
        1: "frenetic random activity period",
        2: "8",
        3: "organo de jacobson",
        4: "manada"
    }
    assert calcular_puntaje(respuestas) == 2

def test_nivel_experto():
    assert nivel_gatero(4) == "Experto en michis"
