#Miguel Jiménez
#Cuenta dígitos


def cuenta(n):
    
    cont=0
    while n>=1:
        n=n//10
        cont+=1
    print(cont)

n=int(input())
cuenta(n)




