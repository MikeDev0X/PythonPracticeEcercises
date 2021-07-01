#ocurrencial de un string

def ocurrencial():
    string1=input('Ingrese el primer string: ')
    string2=input('Ingrese el segundo string: ')
    
    string1.replace(' ','')
    string2.replace(' ','')
    
    lengt=len(string1)
    lengt2=len(string2)
    
    lista=[]
    count=0
    
        
    for i in range(0,lengt):
        if string1[i]==string2[count]:
            count+=1
            
    print(count)
    print(lengt2)
    
    
    n=count//lengt2
    
    if count==lengt2:
        print('ocurrenciales: ', n)
        
    
    
ocurrencial()    
    
    
    