#Crear un programa que imprima en pantalla una tabla de multiplicar utilizando un ciclo for.


numero = int(input("Ingrese un número: "))

print(f"Tabla de multiplicar del {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
