#Miguel Jiménez Padilla



a=float(input())
b=int(input())

if a>10000 and b==1:
    print('1')
elif a>10000 and b==0:
    print ('1')
elif a>=5000 and a<=10000 and b==1:
    print('1')
elif a>=5000 and a<=10000 and b==0:
    print('0')
elif a<5000 and b==1:
    print('0')
else:
    print('0')

