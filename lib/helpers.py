import random
from models import session, Player, Game, Guess

def generate_secret_number():
    digits = list('123456789')
    random.shuffle(digits)
    return ''.join(digits[:4])

def check_guess(secret, guess):
    bulls =0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def create_player(username):
    player = Player(username=username)
    session.add(player)
    session.commit()
    return player

