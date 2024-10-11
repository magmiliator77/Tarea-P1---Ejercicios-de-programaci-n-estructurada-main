#Las tablas de multiplicar: Crea un programa que solicite al usuario un número entre 1 y 10. El programa deberá mostrar la tabla completa de multiplicar de dicho número. Cada salida será del tipo 3x2=6. Al finalizar peguntar si desea ver la tabla de otro número o salir del programa. (1,5 puntos)

salir = 's'


while salir != 'n':
    numeroIntroducido = int(input("Introduce un numero entre 1 y 10 --> "))
    for i in range(1,11):
    
        if numeroIntroducido<=0 or numeroIntroducido>10:
            print(f"ERROR, introduce un numero entre 1-10 ")
            break #rompe el bucle para que solo aparecza el mensaje de error una vez

        else:
        
            print(f"{i} x {numeroIntroducido} = {i * numeroIntroducido}")

    salir = input("¿Desea hacer otra tabla? (s/n)")

       



