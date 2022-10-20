import random

def gioco():
    user = input("Cosa Scegli? 's' per sasso, 'c' per  carta , 'f' per forbice\n")
    cpu = random.choice(['s', 'c', 'f'])

    if user == cpu:
        print ('Siete Pari')

    if hai_vinto(user, cpu):
        print ('Hai Vinto!')

    if hai_vinto(cpu, user):
        print ('Hai Perduto!')
        return gioco()

def hai_vinto(giocatore, avversario):
    #s > f, c > s, f > c
    if (giocatore == 's' and avversario == 'f') or (giocatore == 'c' and avversario == 's') or (giocatore == 'f' and avversario == 'c'):
        return True





print (gioco())