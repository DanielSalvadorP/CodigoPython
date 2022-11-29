from random import randrange
#recibirá una palabra del jugador
palabra= input("scriba la palabra: ")

#contador para que recorra la palabra
for i in range(0,len(palabra)):
   # numLetras=int(len(palabra)/2)
    #print(i)
    parimpar=i%2
    if parimpar==0 :
        print("- "+palabra[i].upper())
    else:
        print("- ")
print("¿Ya sabes cual es la palabra?")
respuesta=input("Dinos cual crees que es: ")
def sw(respuesta):
    if respuesta==palabra :
        print("¡Correcto!")
    else :
        print("¡Incorrecto!")
        respuesta=input("Revisa de nuevo y dinos cual crees que es: ")
        sw(respuesta)
sw(respuesta)
    
