#Crear un programa que reciba una lista de números y calcule la suma de los mismos utilizando un ciclo for

entrada = input("Ingresa una lista de números separados por espacios: ")

numeros = [float(x) for x in entrada.split()]

suma = 0

for numero in numeros:
    suma += numero

print("La suma de los números es: ", suma)