from random import randrange
#el jugador recibirá una palabra de la lista al azar
print("Bienvenido al juego")
puntajetotal=0
puntajeP1=0
puntajeP2=0
puntajeP3=0
p1=""
p2=""
p3=""

for n in range(1,4):
    puntajetotal=int(puntajetotal)-int(puntajetotal)
    player=input("inserta tu nombre: ")

    if n==1:
        p1=player
    if n==2:
        p2=player
    if n==3:
        p3=player
    for j in range(1,5):
        palabra= ["perro","hola","basura","casa","esquisofrenico","burro","cantar","deporte","bailando","latidos","modelo","espalda"]
        palabraelegida=palabra[randrange(12)]
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
        c=True
        def sw(respuesta):
            
            if respuesta==palabraelegida :
                c=True
                return c
            else :
                c=False
                #respuesta=input("Revisa de nuevo y dinos cual crees que es: ")
                #sw(respuesta)
                return(c)
        X=sw(respuesta)
        if X==True:
            print("¡Correcto!")
            puntajetotal=int(puntajetotal)+60
            print(puntajetotal)
        # print("hola") 
            if n==1 :
                puntajeP1=int(puntajetotal)
                #p1=player
                #print(p1+": "+str(puntajeP1))
            if n==2 :
                puntajeP2=int(puntajetotal)
                #p2=player
                #print(p2+": "+str(puntajeP2))
            if n==3 :
                #p3=player
                puntajeP3=int(puntajetotal)
                #print(p3+": "+str(puntajeP3))
        else :
            print("Respuesta incorrecta")
            #puntajetotal=int(puntajetotal)+60
            #print(player+": "+str(puntajetotal))"""
        #puntaje=int(puntajetotal)+0
        #metodo de campeón
        
    print(p1+": "+str(puntajeP1))
    print(p2+": "+str(puntajeP2))
    print(p3+": "+str(puntajeP3))

def campeon() :
    if puntajeP1>=int(puntajeP2) & puntajeP1>=int(puntajeP3) :
        print(f"ganador es {p1.upper()} y su puntaje es {puntajeP1}")
    elif puntajeP2>puntajeP1 & puntajeP2>puntajeP3 :
        print(f"ganador es {p2.upper()} y su puntaje es {puntajeP2}")
    elif puntajeP3>puntajeP1 & puntajeP3>puntajeP2 :
        print(f"ganador es {p3.upper()} y su puntaje es {puntajeP3}")

campeon()
#print(campeon())