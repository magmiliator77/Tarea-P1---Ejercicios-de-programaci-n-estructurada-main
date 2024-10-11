#Usuario y contraseña: Escribe un programa que pida al usuario su nombre y contraseña y le de tres oportunidades para introducir los datos correctos, que serán “smr” (como usuario) y “smr2024” (como clave). Si los datos introducidos son correctos se mostrará por pantalla “Bienvenido/a al sistema”. En caso contrario se mostrará un mensaje por pantalla indicando que se ha superado el número de intentos permitido. (1,5 puntos)


Intentos = 3

while Intentos!=0:
    nombre = str(input("Nombre de usuario: "))
    contraseña = input("Contraseña: ")
    
    if nombre == 'smr' and contraseña == 'smr2024':
        print("Bienvenido/a al sistema :)")
        break
    
    else:
        Intentos -= 1
       
        if Intentos > 0:
            print(f"ERROR, te quedan {Intentos} intentos")
        else:
            print("Has agotado todos tus intentos.")
        


