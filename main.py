import random
import time

while True:
    a=input('pls press enter to roll the dice ')
    print('plss wait')
    
    b=a.lower()

    dice=random.randint(1,6)
    if dice==1:
        n_o_d=1
    if dice==2:
        n_o_d=2
    if dice==3:
        n_o_d=3
    if dice==4:
        n_o_d=4
    if dice==5:
        n_o_d=5
    if dice==6:
        n_o_d=6

    time.sleep(2)
    if b=='':
        print(f'user rolled and got {n_o_d}')
        print()

    elif b=='exit':
        exit()
    else:
        print('**PLS PRESS ENTER**')
        print()
