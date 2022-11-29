from random import randrange
#el jugador recibirá una palabra de la lista al azar
palabra= ["perro","hola","basura","casa","esquisofrenico","burro"]
palabraelegida=palabra[randrange(6)]
#print(palabraelegida)
#contador para que recorra la palabra y mostrará las pistas
for i in range(0,len(palabraelegida)):
   # numLetras=int(len(palabra)/2)
    #print(i)
    parimpar=i%2
    #print(parimpar)
    if parimpar==0 :
        print("- "+palabraelegida[i].upper())
    else:
        print("- ")
print("¿Ya sabes cual es la palabra?")
respuesta=input("Dinos cual crees que es: ")
def sw(respuesta):
    if respuesta==palabraelegida :
        print("¡Correcto!")
    else :
        print("¡Incorrecto!")
        respuesta=input("Revisa de nuevo y dinos cual crees que es: ")
        sw(respuesta)
sw(respuesta)