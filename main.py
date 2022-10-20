# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

##import pygame

import random

def gioco():
    user = input("Cosa Scegli? 's' sasso, 'c'  carta , 'f' forbice\n")
    cpu = random.choice(['s', 'c', 'f'])

    if user == cpu:
        return 'Siete Pari'

    if hai_vinto(user, cpu):
        return 'Hai Vinto!'

    if hai_vinto(cpu, user):
        return 'Hai Perduto!'

def hai_vinto(giocatore, avversario):
    #s > f, c > s, f > c
    if (giocatore == 's' and avversario == 'f') or (giocatore == 'c' and avversario == 's') or (giocatore == 'f' and avversario == 'c'):
        return True

    return gioco()



print (gioco())



