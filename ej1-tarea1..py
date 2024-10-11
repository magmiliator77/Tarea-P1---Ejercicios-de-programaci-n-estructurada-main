#Números impares en un rango: Pide al usuario dos números, uno menor y otro mayor. Controla que el número menos no sea mayor que el número mayor. Escribe un programa que muestre en pantalla los números impares enteros comprendidos entre el número menor y el número mayor (ambos incluidos si son impares). (1,5 puntos)

numeroMenor = int(input("Introduce un numero menor"))

numeroMayor = int(input("Introduce un numero mayor"))


#Controlamos que el numeroMenor no sea mayor o igual que el numeroMayor

if numeroMenor>=numeroMayor:
        print(f"El numero  {numeroMenor} no puede ser menor o igual que {numeroMayor}")
elif numeroMenor % 2 == 1 and numeroMayor % 2 == 1:
        print(f"El {numeroMenor} y el {numeroMayor}  son impares ")
         
else:
        print(f"El {numeroMenor} y el {numeroMayor} son pares")
    
    
for impares in range(numeroMenor, numeroMayor  + 1):

    if impares % 2 ==1:
           print(impares)


