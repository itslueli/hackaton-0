def dividir(a, b):
    """Devuelve la división de dos números. Lanza un error si el divisor es cero."""
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

# Ejemplo de uso
if _name_ == "_main_":
    try:
        resultado = dividir(10, 2)
        print(f"La división de 10 entre 2 es: {resultado}")
    except ValueError as e:
        print(e)