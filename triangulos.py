#Miguel Jiménez Padilla


a=int(input())
b=int(input())
c=int(input())

ab=a+b
ac=a+c
bc=b+c

if ab>c and ac>b and bc>a:
    if a==b and a==c:
        print('EQUILATERO')
    elif a!=b and a!=c:
        print ('ESCALENO')
    elif a==b and a!=c:
        print ('ISOSCELES')
    else:
        print ('ISOSCELES')
else:
    print('NO ES TRIANGULO')



        

