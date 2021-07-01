#numeros primos en un rango de valores

def isPrime(num):
    count=0
    for t in range(1,num+1):
        if num%t==0:
            count+=1
        
    if count==2:
        return True
    else:
        return False


for i in range(1, 20):
    if isPrime(i)==True:
        print(i, end=" ")
