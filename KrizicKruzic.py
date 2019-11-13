polja=[]
brojac=0

for i in range(1,10):
    polja.append(str(i))



def printPolja():
    print('\n -----')
    print('|' + polja[0] + ' ' + polja[1] + ' ' + polja[2] + '|')
    print(' -----')
    print('|' + polja[3] + ' ' + polja[4] + ' ' + polja[5] + '|')
    print(' -----')
    print('|' + polja[6] + ' ' + polja[7] + ' ' + polja[8] + '|')
    print(' -----')



while True:
    printPolja()
    
    if brojac%2==0:
        a=int(input('Igrac 1 na redu: '))
        
        while a<1 or a>9:
            print('Pogresan unos')
            a=int(input('Igrac 1 na redu: '))

        while polja[a-1]=='X' or polja[a-1]=='O':
            print('Pogresan unos')
            a=int(input('Igrac 1 na redu: '))
            
        polja[a-1]='X'
        brojac +=1
        

    else:
        
        a=int(input('Igrac 2 na redu: '))
        
        while a<1 or a>9:
            print('Pogresan unos')
            a=int(input('Igrac 2 na redu: '))

        while polja[a-1]=='X' or polja[a-1]=='O':
            print('Pogresan unos')
            a=int(input('Igrac 2 na redu: '))
        polja[a-1]='O'
        brojac +=1
        

    if('X' in polja[0] and 'X' in polja[1] and 'X' in polja[2]) or ('X' in polja[3] and 'X' in polja[4] and 'X' in polja[5]) or ('X' in polja[6] and 'X' in polja[7] and 'X' in polja[8]) or ('X' in polja[0] and 'X' in polja[3] and 'X' in polja[6]) or ('X' in polja[1] and 'X' in polja[4] and 'X' in polja[7]) or ('X' in polja[2] and 'X' in polja[5] and 'X' in polja[8]) or ('X' in polja[0] and 'X' in polja[4] and 'X' in polja[8]) or ('X' in polja[2] and 'X' in polja[4] and 'X' in polja[6]):
        printPolja()
        print('Pobjednik igrac 1!')
        break

    elif('O' in polja[0] and 'O' in polja[1] and 'O' in polja[2]) or ('O' in polja[3] and 'O' in polja[4] and 'O' in polja[5]) or ('O' in polja[6] and 'O' in polja[7] and 'O' in polja[8]) or ('O' in polja[0] and 'O' in polja[3] and 'O' in polja[6]) or ('O' in polja[1] and 'O' in polja[4] and 'O' in polja[7]) or ('O' in polja[2] and 'O' in polja[5] and 'O' in polja[8]) or ('O' in polja[0] and 'O' in polja[4] and 'O' in polja[8]) or ('O' in polja[2] and 'O' in polja[4] and 'O' in polja[6]):
        printPolja()
        print('Pobjednik igrac 2!')
        break

    if brojac==9:
        print('Nerijeseno')
        break
    
        
        
          
