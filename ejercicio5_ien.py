#determinar el mayor numero de N valores ingresados

n = int(input("Ingrese los valores: "))

lista = [ ]
maximo = 0
minimo = 9999999999999

for i in range(n):
    num = int(input("Ingrese el numero: "))
    lista.insert(i, num)
    lista.sort()
    if num>maximo:
        maximo = num #en cada ciclo, comprobara el if, en caso de ser mayor que el dato guardado en la variable, va a guardar este nuevo dato y asi hasta completar todos lo i posibles de la lista
    if num<minimo:
        minimo = num
    
print(lista)
print("El numero mayor de la lista es: ",maximo)
print("El numero menor de la lista es: ", minimo)