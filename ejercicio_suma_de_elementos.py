#Crear un programa que reciba dos listas de números y que genere una tercera lista que contenga la suma de los elementos de las dos listas en la misma posición, utilizando un ciclo for


def sumar_listas(lista1, lista2):
    
    if len(lista1) != len(lista2):
        return None  

    resultado = []

    for i in range(len(lista1)):
        suma = lista1[i] + lista2[i]
        resultado.append(suma)
    return resultado

lista1 = input("Ingrese la primera lista de números separados por espacios: ").split()
lista2 = input("Ingrese la segunda lista de números separados por espacios: ").split()

lista1 = [int(x) for x in lista1]
lista2 = [int(x) for x in lista2]

resultado = sumar_listas(lista1, lista2)

if resultado is not None:
    print("La lista resultante de la suma es:", resultado)
else:
    print("Las listas no tienen la misma longitud y no se pueden sumar.")
