#Suma mayor que 100: Escribe un programa que vaya solicitando números al usuario hasta que se hayan introducido 10 números o la suma de todos los números leídos sea mayor que 100. A continuación mostrar un mensaje indicando qué condición se ha cumplido (es decir, si se han introducido 10 números o si su suma es mayor que 100. (1,5 puntos)


contador = 0
numero = 0
suma = 0

while contador<10:
    numero = int(input("Introduce un numero --> "))
    if numero != 0:
        suma += numero # Acumulamos la suma de los números introducidos
        print(numero)
        print(f"La suma de los numeros es {suma}")
        contador += 1
        print(f"{contador} numeros introducidos")
    
    if suma >= 100:  # Verificamos si la suma es mayor o igual a 100
        print("La suma de los números introducidos es 100 o más")
        break

    elif numero==0:
        print("ERROR, no puedes introducir el número 0 ya que no suma ningún valor")
        break
    
    
    


