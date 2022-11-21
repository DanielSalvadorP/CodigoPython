print("Bienvenido a MatLib, regalanos una palabra para completar las frases.")
def generador() :
    #Inserts
    print("Inserta un ")
    sust=input("Sustantivo: ")
    sustPlural=input("Sustantivo en plural: ")
    sust2=input("Otro sustantivo: ")
    lugar=input("Lugar: ")
    adjt=input("Adjetivo: ")
    sust3=input("Otro sustantivo: ")

    #Imprimir
    print("El perrito tiene un/a "+sust+" en su collar")
    print("Sin querer, golpee los/as "+sustPlural+" y me lastimé la mano :c")
    print("Acabo de pintar el/la "+sust2+" y quedó muy lindo(a)")
    print("Este(a) "+lugar+" me trae bellos recuerdos")
    print("Ese gatito es muy "+adjt+" y me encanta")
    print("Ese señor tiene un/a "+sust3+" arriba de su sombrero")

generador()
otraVez =input("¿Quieres iniciar de nuevo? Si/No: ")
def switch(otraVez):
    if otraVez == "Si" :
        generador()
        otraVez =input("¿Quieres iniciar de nuevo? Si/No: ")
        switch(otraVez)
    else :
        print("¡Gracias por jugar!")
print(switch(otraVez))