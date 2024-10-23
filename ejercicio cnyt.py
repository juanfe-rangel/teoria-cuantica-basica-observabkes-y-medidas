#seccion 4.1 ejercicio 1
import numpy as np
def calcular_probabilidades(num_posiciones, vector_ket):
    vector_ket = np.array(vector_ket, dtype=np.complex128)
    if vector_ket.size != num_posiciones:
        raise ValueError("El tamaño del vector ket debe ser igual al número de posiciones.")
    
    # Calcula las probabilidades
    probabilidades = np.abs(vector_ket) ** 2
    
    # Normaliza las probabilidades
    probabilidades /= np.sum(probabilidades)
    
    return probabilidades

def probabilidad_en_posicion(probabilidades, posicion):
    # Verifica que la posición esté dentro del rango
    if posicion < 0 or posicion >= len(probabilidades):
        raise ValueError("La posición debe estar dentro del rango de posiciones disponibles.")
    
    return probabilidades[posicion]

num_posiciones = 6
vector_ket = [2-1j, 2j, 1-1j, 1, -2j, 2]

probabilidades = calcular_probabilidades(num_posiciones, vector_ket) #probabilidad cada espacio
print("Probabilidades de encontrar la partícula en cada posición:", probabilidades)

posicion_a_verificar = 3
probabilidad = probabilidad_en_posicion(probabilidades, posicion_a_verificar)

print(f"La probabilidad de encontrar la partícula en la posición {posicion_a_verificar} es: {probabilidad:.4f}")

#seccion 4.1 ejercicio 2
import numpy as np
def calcular_probabilidades(num_posiciones, vector_ket):
    vector_ket = np.array(vector_ket, dtype=np.complex128)
    
    if vector_ket.size != num_posiciones:
        raise ValueError("El tamaño del vector ket debe ser igual al número de posiciones.")
    
    probabilidades = np.abs(vector_ket) ** 2
    probabilidades /= np.sum(probabilidades)
    
    return probabilidades

def calcular_probabilidad_transicion(vector_ket1, vector_ket2):
    if len(vector_ket1) != len(vector_ket2):
        raise ValueError("Ambos vectores deben tener el mismo tamaño.")

    producto_interno = np.dot(vector_ket1, np.conj(vector_ket2))
    
    probabilidad_transicion = np.abs(producto_interno) ** 2
    
    return probabilidad_transicion

num_posiciones = 6
vector_ket1 = [2-1j, 2j, 1-1j, 1, -2j, 2]  
vector_ket2 = [1, 1, 0, 0, 0, 0]           

probabilidades1 = calcular_probabilidades(num_posiciones, vector_ket1)

probabilidades2 = calcular_probabilidades(num_posiciones, vector_ket2)

print("Probabilidades del primer vector:", probabilidades1)
print("Probabilidades del segundo vector:", probabilidades2)

probabilidad_transicion = calcular_probabilidad_transicion(vector_ket1, vector_ket2)

print(f"La probabilidad de transitar del primer vector al segundo es: {probabilidad_transicion:.4f}")