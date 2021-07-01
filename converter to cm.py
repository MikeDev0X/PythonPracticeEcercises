def feet():
    feet=int(input('Feet: '))
    if feet<=0:
        print('Error')
    else:
        print ('cm: ',feet*30.48)

def inches():
    inches=int(input('Inches: '))
    if inches<=0:
        print('Error')
    else:
        print ('cm: ',inches*2.54)

def yards():
    yards=int(input('Yards: '))
    if yards<=0:
        print('Error')
    else:
     print('cm: ',yards*91.44)

def user():
    
    while True:
        user=int(input('\nMenu:\n1.Feet\n2.Inches\n3.Yards\n0.Exit\n '))
        if user==1:
            feet()
        elif user==2:
            inches()
        elif user==3:
            yards()
        elif user==0:
            print('see you later :)')
            break
        else:
            print('Error, try again')
user()
