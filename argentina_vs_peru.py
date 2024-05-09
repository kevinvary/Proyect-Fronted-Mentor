#contar los votos

personas_a_votar = int(input("Cantidad de participantes: "))
print("Peru-->Opcion.1")
print("Argentina-->Opcion.2")
contador_arg = 0
contador_peru = 0
for i in range(1, personas_a_votar+1):
    voto = int(input(f"Asistente numero {i}: "))
    while voto < 1 or voto > 2:
        print("Ingrese opciones correspondientes")
        voto = int(input(f"Asistente numero {i}: "))
    if voto==1:
        contador_arg = contador_arg + 1
    if voto==2:
        contador_peru = contador_peru + 1

if contador_arg > contador_peru:
    print("El ganador es Argentina")
else:
    print("El gandor es Peru")


print("Los votos para peru son: ", contador_peru)
print("Los votos para argentina son: ", contador_arg)
        
    