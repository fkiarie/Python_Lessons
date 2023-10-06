import random

def get_choices():
    player_choice = input("Enter a choice(Rock, Paper, Choices)")
    option = ['Rock', 'Paper', 'Choices']
    computer_choice = random.choice(option)
    choices = {'player': player_choice, 'computer': computer_choice}

    return choices
def check_win(player, computer):
    print(f'You choose {player} and the computer choose {computer}')
    if player == computer:
        return "Its a tie"
    elif player == "Rock":
        if computer == "Scissors":
            return "Rock smashes scissors. You win!"
        else:
            return "Paper covers rock. You lose!"
    elif player == "paper":
        if computer == "Rock":
            return "Paper covers rock. You Win!"
        else:
            return "Scissor cuts paper. You lose!"
    elif player == "Scissors":
        if computer == "Paper":
            return "Scissor cuts paper. You win!"
        else:
            return "Rock smashes scissors. You lose!"

choices = get_choices()
result = check_win(choices['player'], choices['computer'])

print(result)