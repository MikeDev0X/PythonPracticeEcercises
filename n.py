#Miguel Jiménez, Gabdiel Adame
#Sumatoria de 1 a n

numero = int(input())
def sumatoria(num):
    contador = 2
    ms='1'
    sumas = 1
    ns = 3
    print('1=1')
    while contador<=num:
        
        ms=ms+'+'+str(contador)
        print(ms+'='+str(ns))
        contador+=1
        sumas=sumas+ns
        ns=ns+contador
        
    return sumas


suma=sumatoria(numero)
print("La suma de la serie hasta el número " +str(numero) +" es: " + str(suma))