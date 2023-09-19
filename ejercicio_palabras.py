#Crear un programa que reciba una lista de palabras y muestre únicamente aquellas que empiezan con una letra determinada, utilizando un ciclo for y una estructura condicional if.

letra_inicial = input("Ingrese una letra: ").lower()  
palabras = input("Ingrese una lista de palabras separadas por espacios: ").split()

print(f"Lista de palabras con la letra seleccionada anteriormente: {letra_inicial} \n")
for palabra in palabras:
   if palabra.lower().startswith(letra_inicial):
        print(palabra)
