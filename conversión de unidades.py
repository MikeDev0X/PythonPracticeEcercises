#Miguel Jiménez Padilla

a=int(input())

if a<100 and a>0:
    print(a , 'cm')
elif a>=100 and a<1000:
    print(((a-(a%100))/100),'m')
    print(a%100,'cm')
else:
    if a%100000>=1000:
        print(((a-(a%100000))/100000), 'km')
        z=(a%100000)
        print((((z)-(z%100))/100),'m')
        x=((z%100))
        if (x)>0 and (x)<100:
            print(((x)),'cm')
    else:
        print(((a-(a%100000))/100000), 'km')
        i=(a%100000)
        if (i)>=100 and (i)<1000:
            print ((((i)-(a%100))/100),'m')
            if ((i)%100)>0 and ((i)%100)<100:
                print((a%100),'cm')
        else:
            print(a%100, 'cm')
        
        
      
