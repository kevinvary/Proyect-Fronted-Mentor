#desarrolla un programa que cuenta las vocales de una oracion


frase = input("Ingrese una frase: ")

contador = 0

for i in frase:
    if i in "aeiou":
        contador +=1


print("Las vocales totales en la frase es de: ", contador)