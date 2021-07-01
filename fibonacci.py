#Miguel Jiménez, Gabdiel Adame
#Secuencia de Fibonacci

index = int(input())

def fibonacci_index(z):
    if z <= 0:
        return 
    elif z == 1:
        return int('0')
    elif z == 2:
        return int('1')
    else:
        a = 0
        b = 1
        c = 0
        while z > 2:

            c = a + b
            a = b
            b = c

            z -= 1
        return c

result = fibonacci_index(index)
print(result)
