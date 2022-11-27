from random import randrange, choice
#inicio
#Ingresa un numero
print("""Adivina el número
Recuerda, cada vez que falles, el número cambiará""")
def Random():
    k=int(input("Inregresa un numero del 0 al 10: "))
    s=randrange(10)
    #print(s)
    if k==s :
        print("¡Correcto!")
    else:
        print("va de nuevo")
        Random()
Random()

