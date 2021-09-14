from src.prueba import tableroVacio

def test_tablero_vacio_tiene_6_filas():
    tablero = tableroVacio()

    assert len(tablero) == 6