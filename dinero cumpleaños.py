#Miguel Jiménez Padilla
#Dinero cumpleaños


def dineroCumpleaños(n):
    dinero=10

    while dinero<=1000:
        dinero=dinero*2
        n=n+1
    print(n, dinero)

n=int(input())
dineroCumpleaños(n)