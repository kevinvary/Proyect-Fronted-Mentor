#escribe un algoritmo que tome una lista de numeros como entrada
#y devuelva la suma de todos los elementos


numeros_a_ingresar = int(input("Ingrese la cantidad de numeros: "))

suma = 0

for i in range(numeros_a_ingresar):
    n = int(input("Digite un numero: "))
    suma = suma + n
    

print("La cantidad de la suma de todos los elementos, es de: ", suma)
