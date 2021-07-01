#Miguel Jiménez Padilla

a=int(input())

if a==0 or a==90 or a==180 or a==270 or a==360:
    print('eje')
elif a>0 and a<90:
    print('cuadrante 1')
elif a>90 and a<180:
    print ('cuadrante 2')
elif a>180 and a<270:
    print ('cuadrante 3')
elif a>270 and a<360:
    print ('cuadrante 4')
else:
    print('excede')
    

