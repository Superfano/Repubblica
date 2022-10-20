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



