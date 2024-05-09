#calcular el producto de todos los n numeros ingresados, el producto
#de los pares y el producto de los impares

numeros_a_ingresar = int(input("ingrese la cantidad: "))

i=1
producto = 1
impar = 1
par = 1
for i in range(numeros_a_ingresar):
    num = int(input("Ingrese el numero: "))
    producto = producto * num
    if num%2!=0:
        impar = impar*num
    else:
        par = par*num

print("El producto de todos los numeros es: ", producto)
print("El producto de todos los numeros impares es: ", impar)
print("El producto de todos los numeros pares es: ", par)