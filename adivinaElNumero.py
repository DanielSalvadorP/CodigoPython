from random import randrange 
#inicio
#Ingresa un numero
print("""Adivina el número
Recuerda, cada vez que falles, el número cambiará""")
def Random():
    k=int(input("Inregresa un numero: "))
    s=randrange(7)
    if k==s :
        print("¡Correcto!")
    else:
        print("va de nuevo")
        Random()
Random()