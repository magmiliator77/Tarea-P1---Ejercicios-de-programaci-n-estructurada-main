#Números pares de 3 cifras: Escriba un programa que solicite al usuario números positivos de tres o más cifras y compruebe si son pares, indicando por pantalla “Es un número par” o “No es un número par”. Si el número introducido es positivo pero de una o dos cifras, se solicitará un nuevo número. El programa finaliza cuando se introduce “0” o un número negativo. (1,5 puntos)

numero = 1  # Inicializamos en un valor positivo mayor a 0

while numero != 0 and numero > 0:  # El ciclo continúa hasta que se introduce 0 o un número negativo
    numero = int(input("Introduce un número de 3 o más cifras que sea positivo (o 0 para salir) --> "))
    
    if numero == 0 or numero < 0:  # Condición para salir del ciclo
        print("Programa finalizado.")
        break
    
    if numero < 100:  # Verificamos si el número tiene al menos 3 cifras
        print("ERROR, introduce un número de 3 o más cifras.")
        continue  # Volvemos a solicitar el número
    
    if numero % 2 == 0:  # Verificamos si el número es par
        print("El número es par.")
    else:
        print("El número no es par.")




    