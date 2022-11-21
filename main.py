#comentarios
"""
comentarios
en
bloque
"""
#Inicio
#print("Hola mundo")

#Variables
"""
texto = "Repaso de python"
nombre = "Daniel Alexander Salvador"
altura = "165cm" 
año = 2022 

print(texto)
print(año) #imprime lo contenido en año como un entero
print(str(año)) #imprime lo contenido en año como un string)
print(f"{texto} - {nombre} - {altura} - {str(año)}") #variables concatenadas por f
print(texto +" - "+ nombre +" - "+ altura+" - "+str(año))
#cls para limpiar consola
"""

#Entrada
"""print("Hola mundo") #imprimir
hola= input("Hola :") #recibir por consola
print(hola)
"""

#Condiciones
"""
print("Digita tu altura :")
altura = input()    
if int(altura) >= 180 :
    print("Eres alto")
else:
    print("Eres bajito")
"""

#Funciones   - def para definir
"""#para que me pregunte una edad cada vez que llame la función
def mostrarFunciones(): #Tener cuidado al tabu
    lar las lineas
    #print("Digita tu altura :")
    altura = int(input("Digita tu altura :"))   
    if (altura) >= 180 :
        print("Eres alto")
    else:
        print("Eres bajito")
    return altura

mostrarFunciones()
"""
"""
var_altura = int(input("Digita tu altura :"))  
def mostrarFunciones2(altura): #Tener cuidado al tabular las lineas
    resultado=""
    if (altura) >= 180 :
        resultado="Eres alto"
    else:
        resultado="Eres bajito"
    return resultado

#mostrarFunciones2(var_altura) cuando solo queremos imprimir el resultado
print(mostrarFunciones2(var_altura)) #cuando tenemos un retorno en la función
"""

#listas
personas=["Victor", "Paco", "Pedro"]
print(personas)#imprimir toda la lista
print(personas[1])#imprimir el contenido de una posición en especifico
#for para recorrer y mostrar el contenido de la lista
for persona in personas:
    print("- "+persona)
