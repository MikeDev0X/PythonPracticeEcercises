#Miguel Jiménez Padilla
#Factorial

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        i=1
        fac=1
        
        if n>1:
            while i!=n:
                
                fac=fac*i
                i+=1
            fac=fac*n    
            return fac
        
        else:
            return 'Factorial no definido para negativos'


r=(factorial(int(input())))
print(r)
