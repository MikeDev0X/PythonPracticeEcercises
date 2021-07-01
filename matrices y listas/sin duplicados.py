'''Miguel Jiménez Padilla
Sin duplicados'''

def sinDup():
    elem=int(input())
    if elem>0:
        lista=[]
        num=''
        for i in range (0,elem):
            num=input()
            lista.append(num)

        newlist=[]
        for x in lista:
            if not x in newlist:
                newlist.append(x)
        
        print(lista)
        print(newlist)
    else:
        print('Error')
    
sinDup()
