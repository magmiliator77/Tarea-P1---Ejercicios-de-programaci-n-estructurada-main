#Adivinar un número entre 1 y 100: Escribir un programa para adivinar un número entre 1 y 100 que previamente se ha definido en una variable interna. El programa irá pidiendo números al usuario y, siempre que dicho número no coincida con el número secreto, le indicará si el número introducido es mayor o menor que el número secreto que tiene que adivinar. Al final, el programa indicará la cantidad de intentos que se han necesitado para adivinar el número. Si el número de intentos es menor que 5 se mostrará “Enhorabuena!”. Si es un valor entre 5 y 10 se mostrará el mensaje “No está mal”. Si el número de intentos es mayor que 10 se mostrará el mensaje “Debe practicar más”. (1,5 puntos)


from random import *

numeroCorrecto = 10 #Un numero al azar entre 1 y 100
numeroIntroducido = str(input("presiona s para empezar --> "))  #Esto como tal no hace ahora mismo, solo para inicializar la variable
Intentos = 0

while numeroIntroducido != numeroCorrecto:
    numeroIntroducido = int(input("Introduce un número entre el 1-100 --> "))
    Intentos += 1

    if numeroIntroducido < numeroCorrecto:
        print("Te has quedado corto...")
        
    elif numeroIntroducido > numeroCorrecto:
        print("Te has pasado...")
        
    else:
        if Intentos < 5:
            print("Enhorabuena!")
        elif Intentos>=5 and Intentos<=10:
            print("No está mal")

        elif Intentos>10:
         print("Debe practicar más")
