#Crea una lista de 5 nombres de frutas.
#Utiliza un ciclo for para imprimir en pantalla cada uno de los nombres de la lista.
#Utiliza otro ciclo for para imprimir en pantalla cada letra de cada uno de los nombres de la lista.


frutas = ["Manzana", "Mango", "Pera", "Uva", "Fresa"]
print ("Lista de frutas:\n")
for indice, fruta in enumerate (frutas, 1):
    print(f"{indice}, {fruta}")
print("\nLetras de los nombres de frutas:\n")   
for fruta in frutas:
    for letra in fruta:
        print(letra)
    print()