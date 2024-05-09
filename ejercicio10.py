#ingresar un numero y determinar si es un numero primo o si no lo es


n = int(input("Ingrese un numero: "))
contador = 0
for i in range(1, n+1):
    if n%i==0: #Este bucle for, lo que hace es, recorrer desde 1 hasta n+1 tratando de buscar divisores del numero n, cuando encuentre un divisor, añade un nuevo calor al contador y sigue buscando otro divisor, hasta encontrar otro y actualizar de nuevo el contdor
        contador += 1

if contador>2:
    print("El numero ", n, "no es un numero primo")
else:
    print("El numero ", n, "es primo")

        