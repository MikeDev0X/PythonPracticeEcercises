#Miguel Jiménez Padilla
#palíndromo


def pal():
    dato=input()
    dato=dato.replace(' ','')
    dato=dato.lower()
    long=len(dato)
    newS=''
    count=long
    
    for i in range (long,0,-1):
        newS=newS+dato[count-1]
        count=count-1
    
    if dato==newS:
        print('Es un palindromo')
    else:
        print('NO es un palindromo')

pal()









