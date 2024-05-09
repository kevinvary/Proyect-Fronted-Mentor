#ejercicio 6 en python
#mostrar con un while los numeros del 1 al 100


numerosUnoAlCien = 99

while (numerosUnoAlCien <= 100 ):
    print(numerosUnoAlCien, end=" ")
    numerosUnoAlCien+=1

#uno al 100 con for
for i in range(1, 10,5):
    print(i)
    

#recorrer cadenas con for

for i in ("Hola mundo"):
    print(i)
    
#mostras los numeros pares entre 1 y 100 con for sin if
for i in range(2,101, 2):
    print(i)
    
#mostrar los numeros pares entre 1 y 100 con for usando if

for i in range(1,101):
    if((i%2)==0): #le pido que me devuelva las divisiones con resto 2
        print(i)