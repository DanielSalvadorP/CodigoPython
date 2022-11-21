num=int(input("¿En que número estás pensando? "))
def parImpar (num):
    resultado=num%2

    if resultado==0 :
        print("¡Es un numero par!")
    else :
        print("¡Es un número impar!")
    
parImpar(num)
deNuevo=input("¿Puedes añadir otro? Si/No: " )

def switch(deNuevo) :
    if deNuevo == "Si" :
        num=int(input("¿En que número estás pensando? "))
        parImpar(num)
        deNuevo=input("¿Puedes añadir otro? Si/No: " )
        switch(deNuevo)        
    elif deNuevo == "No" :
        print("¡Gracias!")
    else :
        print("Respuesta Incorrecta")
print(switch(deNuevo))
