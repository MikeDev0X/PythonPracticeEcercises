#Miguel Jiménez

def es_bisiesto():
    a=int(input())
    if a%4==0 and a%100!=0 :
        print('True')
    elif a%100==0 and a%400==0:
        print('True')
    else:
        print('False')

es_bisiesto()
    












