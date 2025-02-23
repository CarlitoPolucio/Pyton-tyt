def rock_paper_scissors():
    play_choice = input("Enter ""rock"", ""Paper"", or ""scissors"": ")
    pc_secret = "rock"
    win = "You are win"
    lose = "You are lose"
    if play_choice == pc_secret:
        return "draw"
    elif play_choice == "scissors" and pc_secret == "rock":
        return lose
    elif play_choice == "scissors" and pc_secret == "paper":
        return win
    elif play_choice == "paper" and pc_secret == "rock":
        return win
    elif play_choice == "paper" and pc_secret == "scissors":
        return lose
    elif play_choice == "rock" and pc_secret == "scissors":
        return win
    else:
        return lose


def guess_the_number():
    pc_secret = 1
    guess = 0
    while guess != pc_secret:
        guess = int(input("Enter the num: "))
    return "You are win"


def main_menu():
    choice = input("what do you want to play? ""Rock, paper, scissors""(1) "
                   "or ""Guess the number""(2)?: ")
    if choice == "1":
        print(rock_paper_scissors())
        return main_menu()
    else:
        print(guess_the_number())
        return main_menu()


main_menu()
