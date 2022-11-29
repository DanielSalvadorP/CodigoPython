from random import randrange
#el jugador recibirá una palabra de la lista al azar

for n in range(1,4):
    if n==1:
        player=input("inserta tu nombre: ")
    if n==2:
        player=input("inserta tu nombre: ")
    if n==3:
        player=input("inserta tu nombre: ")
    
    palabra= ["perro","hola","basura","casa","esquisofrenico","burro","cantar","deporte","bailando","latidos","modelo","espalda"]
    palabraelegida=palabra[randrange(12)]
    print(palabraelegida)
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
    puntaje=0
    puntajetotal=0
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
    sw(respuesta)
    if c==True:
        print(c)
        puntajetotal=int(puntajetotal)+60
        print(player+": "+str(puntajetotal))
        if n==1 :
            punatajeP1=int(puntajetotal)
        
    else :
        print(c)
        #puntajetotal=int(puntajetotal)+60
        print(player+": "+str(puntajetotal))
    #puntaje=int(puntajetotal)+0