import random

def play():
    user = input(f"What is your choice?\n'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return f"You win! The computer chose '{computer}'"
    
    return f"You lost! The computer chose '{computer}'"

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())