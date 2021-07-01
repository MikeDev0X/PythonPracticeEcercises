#Miguel Jiménez Padilla
#Locura

#-*- coding: utf-8 -*-
def locura():
    cad=input()
    cad=cad.lower()
    lengt=int(len(cad))
    rec=0
    varF=''
    count=''
    
    for i in range(0,lengt):
        if cad[rec]=='a' or cad[rec]=='á':
            varF='4'
        elif cad[rec]=='e':
            varF='3'
        elif cad[rec]=='o':
            varF='h'
        else:
            varF=cad[rec]
        count=count+varF
        rec=rec+1
       
    print(count)
    
locura()