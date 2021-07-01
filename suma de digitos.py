#Miguel Jiménez Padilla
#Suma de dígitos

def suma_digitos(n):
    
    if n<0:
        n=n*(-1)
    digitos=0
    while n>=1 or n<=-1:
        
        d=n%10
        digitos=digitos+d
        n=n//10
        
    print(digitos)

n=int(input())
suma_digitos(n)




