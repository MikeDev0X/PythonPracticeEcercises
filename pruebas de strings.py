#Miguel Jiménez Padilla


def pide():
    string=input('give me a string\n')
    print('tu cadena tiene: {}'.format(len(string)))





def contar():
    voc=input('give me a string\n')
    voc=voc.lower()
    count=1
    for i in voc:
        if voc in ['a','e','i','o','u']:
            count=count+1
    print(count)






def x():
    cad=input('Entrada: ')
    cad=cad.lower()
    rem=cad[0]
    
    var=cad[1:len(cad)].replace(rem,'*')
    print(rem+var)
    
    
x()
    
    
    
    
    
    