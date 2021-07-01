

def multiplicacion(n1,n2):
    m=n1*n2
    print('multiplicación: ', m)
        
def division(n1,n2):
    if n1>n2:
        d=n1/n2
    elif n2>n1:
        d=n2/n1
    else:
        d=n1/n2
        
    print('división: ', d)
            
def resta(n1,n2):
        
    if n1>n2:
        d=n1-n2
    elif n2>n1:
        d=n2-n1
    else:
        d=n1-n2
    print('resta: ', d)
        
def suma(n1,n2):
    s=n1+n2
    print('suma: ', s)
    
def main():
    n1=1
    n2=1
    while n1!=0 or n2!=0:
        n1=int(input('Ingrese el primer número: \n si desea terminar el programa ingrese 0: '))
        if n1==0:
            return None
        
        
        
        else:
            n2=int(input('Ingrese el segundo número: \n si desea terminar el programa ingrese 0: '))
            if n2==0:
                return None
            suma(n1,n2)
            resta(n1,n2)
            multiplicacion(n1,n2)
            division(n1,n2)
        
        
        
main()


        