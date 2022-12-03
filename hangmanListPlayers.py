from random import randrange
#el jugador recibirá una palabra de la lista al azar
print("Bienvenido al juego")
puntajetotal=0
palabraelegida=""
puntajes=[]
players=[]
numPlayers=input("¿Cuantos van a jugar?:")
palabra= ["perro","hola","basura","casa","esquisofrenico","burro","cantar","deporte","bailando","latidos","modelo","espalda"]

#recolección de datos
def inicio(numPlayers):
    for l in range(0,int(numPlayers)):
        namPlayer=input(f"nombre del jugador {l+1}: ")
        players.append(namPlayer)
    return players

#estructra del juego
def jugar():
    puntajetotal=0
    for j in range(0,5):
        print(f"palabra {j+1}")
        palabraelegida=palabra[randrange(12)]
        
        #contador para que recorra la palabra y mostrará las pistas
        for i in range(0,len(palabraelegida)):
            parimpar=i%2
            if parimpar==0 :
                print("- "+palabraelegida[i].upper())
            else:
                print("- ")
                
        print("¿Ya sabes cual es la palabra?")
        respuesta=input("Dinos cual crees que es: ")
        #comprobar
        if respuesta==palabraelegida :
            print("¡Correcto!")
            puntajetotal=int(puntajetotal)+60
        else :
            print("Respuesta incorrecta")
        print("-------------------------------------------")
    #agregar puntos a la lista de los puntos
    puntajes.append(puntajetotal)
    print("Fin del turno")
    print("-------------------------------------------------")
    
              
inicio(numPlayers)
for l in (0,numPlayers):
    jugar()
for z in range(0,int(numPlayers)):
    print("El puntaje de " +players[z].upper()+" es "+ str(puntajes[z]))

