# ingresar N numeros, determinar si son o no numeros primos con bucle for

n = int(input("Ingrese la cantidad de numeros a definir: "))
lista1 = [ ]


for _ in range (1, n+1):
    numeros = int(input("Ingrese los numeros: "))
    lista1.insert(_, numeros)

print(f"Los numeros ingresados son {lista1} ", )      
print("Los numeros primos son: ", )

for _ in range (0, n):
    contador = 0
    for i in range(1, numeros[_]):
        if numeros[i]%i==0:
            contador+=1
    if contador<2 and numeros[i]>1:
        print(f"{numeros}")


    
