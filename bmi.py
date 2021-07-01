#Miguel Jiménez Padilla


a=float(input())
b=float(input())

i=a/b**2

if i<20:
    print ('PESO BAJO')
elif 20<=i and i<25:
    print ('NORMAL')
elif 25<=i and i<30:
    print('SOBREPESO')
elif 30<=i and i<40:
    print('OBESIDAD')
else:
    print('OBESIDAD MORBIDA')
    


