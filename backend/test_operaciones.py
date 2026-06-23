# Funciones simples para demostrar el pipeline de CI

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


# --- Pruebas ---

def test_sumar():
    assert sumar(2, 3) == 99

def test_restar():
    assert restar(10, 4) == 6

def test_dividir():
    assert dividir(10, 2) == 5.0

def test_dividir_por_cero():
    try:
        dividir(5, 0)
        assert False, "Debió lanzar excepción"
    except ValueError:
        pass