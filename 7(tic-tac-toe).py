import random
print('Τρίλιζα\n Εσείς Έχεται Το Χ Και Ο Υπολογιστής Το Ο.')
l = [None]*9
for i in range(9):
    l[i] = '_'
    print (l[i],' ',end='')
    if(i==2 or i==5 or i==8):
        print ('\n')
a=True
while a==True:
    inp = input('Εισάγεται Ενάν Αριθμό(0-8):')
    while inp.isdigit() != True:
            inp = input('Διαλέξτε Μόνο Αριθμούς:')
    j = int(inp)
    while j>8:
        j = int(input('Επιλέξετε Άλλη Θέση:'))
    while(l[j]=='X' or l[j]=='O'):
        j = int(input('Επιλέξετε Άλλη Θέση:'))
    l[j] = 'X'
    if(l[0]==l[1] and l[0]==l[2] and l[1]==l[2] and l[0]=='X') or (l[3]==l[4] and l[3]==l[5] and l[4]==l[5] and l[3]=='X') or (l[6]==l[7] and l[6]==l[8] and l[7]==l[8] and l[6]=='X') or (l[0]==l[3] and l[0]==l[6] and l[6]==l[3] and l[0]=='X') or (l[1]==l[4] and l[1]==l[7] and l[4]==l[7] and l[1]=='X') or (l[2]==l[5] and l[2]==l[8] and l[5]==l[8] and l[2]=='X') or (l[0]==l[4] and l[0]==l[8] and l[4]==l[8] and l[0]=='X') or (l[2]==l[4] and l[2]==l[6] and l[4]==l[6] and l[2]=='X'):
        for i in range(9):
            print (l[i],' ',end='')
            if(i==2 or i==5 or i==8):
                print ('\n')
        print('Κερδίσατε')
        break
    if(l[0]!='_' and l[1]!='_' and l[2]!='_' and l[3]!='_' and l[4]!='_' and l[5]!='_' and l[6]!='_' and l[7]!='_' and l[8]!='_'):
        for i in range(9):
            print (l[i],' ',end='')
            if(i==2 or i==5 or i==8):
                print ('\n')
        print('Δεν Υπάρχει Νικητής')
        break
    n = random.randint(0,8)
    while(l[n]=='X' or l[n]=='O'):
        n = random.randint(0,8)
    l[n] = 'O'
    for i in range(9):
        print (l[i],' ',end='')
        if(i==2 or i==5 or i==8):
            print ('\n')
    if(l[0]==l[1] and l[0]==l[2] and l[1]==l[2] and l[0]=='O') or (l[3]==l[4] and l[3]==l[5] and l[4]==l[5] and l[3]=='O') or (l[6]==l[7] and l[6]==l[8] and l[7]==l[8] and l[6]=='O') or (l[0]==l[3] and l[0]==l[6] and l[6]==l[3] and l[0]=='O') or (l[1]==l[4] and l[1]==l[7] and l[4]==l[7] and l[1]=='O') or (l[2]==l[5] and l[2]==l[8] and l[5]==l[8] and l[2]=='O') or (l[0]==l[4] and l[0]==l[8] and l[4]==l[8] and l[0]=='O') or (l[2]==l[4] and l[2]==l[6] and l[4]==l[6] and l[2]=='O'):
        print('Χάσατε')
        break
