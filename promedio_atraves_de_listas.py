#ingresar 4 notas, mostrarlos en una lista y calcular el promedio

lista = [ ]
suma = 0
for m in range(4):
    nota = int(input("Ingrese las nota: "))
    lista.insert(m, nota)
    suma += lista[m]


promedio_lista = suma / 4
    
print(lista)
print("El promedio de la lista es de: ", promedio_lista)