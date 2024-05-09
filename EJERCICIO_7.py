#ingresar n notas, mostrarlos en una lista y calcular el
#prodicto de todos sus valores


n = int(input("Ingrese la cantidad de notas: "))
lista_notas = [ ]
producto = 1
for i in range (n):
    notas = int(input("Ingrese la nota:  "))
    lista_notas.insert(i, notas) #con insert, creo elementos dentro de la lista
    producto *= lista_notas[i]
print(lista_notas)
print("El resultado de multiplicar todas las notas es de: ", producto)