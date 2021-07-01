#Miguel Jiménez Padilla
#Números primos

def primos(n):
    
    if n==0 or n==1:
        return False
    elif n==2:
        return True
        
    else:
            
        for i in range(2,n):
            
            if n%i==0:
                return False
            return True

n=abs(int(input()))
print(primos(n))
