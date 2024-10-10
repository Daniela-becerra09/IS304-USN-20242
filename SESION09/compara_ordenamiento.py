def tuplas(entrada):
    # Verificamos que la entrada sea una tupla
    if not isinstance(entrada, tuple):
        raise ValueError("La entrada debe ser una tupla.")
    
    # Ordenamos la tupla y devolvemos una nueva tupla
    return tuple(sorted(entrada))

# Ejemplo de uso
entrada = (3, 1, 4, 2)
resultado = tuplas(entrada)
print(resultado)  # Salida: (1, 2, 3, 4)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import time
import random

def tuplas(entrada, medir_tiempo=False):
    # Verificamos que la entrada sea una tupla
    if not isinstance(entrada, tuple):
        raise ValueError("La entrada debe ser una tupla.")
    
    if medir_tiempo:
        start_time = time.time()  # Inicia el cronómetro
    
    # Ordenamos la tupla y devolvemos una nueva tupla
    resultado = tuple(sorted(entrada))
    
    if medir_tiempo:
        end_time = time.time()  # Termina el cronómetro
        tiempo_total = end_time - start_time
        print(f"Tiempo de ejecución: {tiempo_total:.6f} segundos")
    
    return resultado

# Generamos una tupla con 10,000 datos aleatorios
entrada = tuple(random.randint(1, 10000) for _ in range(10000))

# Llamamos a la función con el parámetro `medir_tiempo=True`
resultado = tuplas(entrada, medir_tiempo=True)
