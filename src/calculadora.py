def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

def operacion_compleja(n):
    # Código con un poco de complejidad para que SonarCloud lo detecte
    resultado = 0
    for i in range(n):
        if i % 2 == 0:
            resultado += i * 2
        else:
            resultado -= i
    return resultado
