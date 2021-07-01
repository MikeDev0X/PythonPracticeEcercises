#Miguel Jiménez Padilla

def cuadrado_n (n):
    cont=0
    for i in range (n, 0,-1):
        c=n**2
        cont=cont+c
        n=n-1
    print(cont)
    
n=int(input())
cuadrado_n(n)