#Miguel Jiménez, Gabdiel Adame
# Sumatoria Secuencial hasta N

n=int(input())
suma = 0
x=1

for z in range(n):
    
    if z <= 0:
        return "error"
    elif z>0:
        a = 0
        b = 1
        c = 0
        for z in range(2,n):

            c = a + b
            a = b
            b = c

            z -= 1
        return c
    
    
    
    
    
print(n)



















