loop=1
print("Inicia el conteo:")
contador=0

for i in range(2,10):
    print(i)
    for n in range(2,i):
        if i%n==0 : 
            contador+=1
            print("Divisor: "+str(n))
    if contador>0 :
        print("No es primo")
    else :
        print("Es primo")
    contador=0

    