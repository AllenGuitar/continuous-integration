# Validacion de testeos en base al programa

from quiz_gatitos import verificar_respuesta, calcular_puntaje, nivel_michi, obtener_pregunta, obtener_total_preguntas

def test_frap_correcto():
    assert verificar_respuesta(1, "frenetic random activity period") == True

def test_frap_incorrecto():
    assert verificar_respuesta(1, "free runing animal period") == False

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
    assert nivel_michi(4) == "Experto en michis"

def test_total_preguntas():
    assert obtener_total_preguntas() == 4