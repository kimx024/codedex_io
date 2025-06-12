import random

def rock_paper_scissors():
    while True:
        print(
            "===================\n"
            "Rock Paper Scissors\n"
            "===================\n"
            "1) ✊ (Rock)\n"
            "2) ✋ (Paper)\n"
            "3) ✌️ (Scissors)\n"
        )

        try:
            player = int(input("Pick a number: "))
            if player not in [1, 2, 3]:
                print("Invalid input. Please choose 1, 2, or 3.\n")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        computer = random.randint(1, 3)
        choices = {1: "✊", 2: "✋", 3: "✌️"}

        print(f'Player chose: {choices[player]}')
        print(f'CPU chose: {choices[computer]}')

        if player == computer:
            print("It's a tie!\n")
        elif (player == 1 and computer == 3) or \
                (player == 2 and computer == 1) or \
                (player == 3 and computer == 2):
            print("The player won!\n")
        else:
            print("The CPU won!\n")

        answer = input("Stop game? (yes/y to stop, no/n to continue, switch/s to switch game): ").strip().lower()
        if answer == "yes" or answer == "y":
            break
        elif answer == "switch" or answer == "s":
            rock_paper_scissors_lizard_spock()
            break



def rock_paper_scissors_lizard_spock():
    while True:
        print(
            "===================\n"
            "Rock Paper Scissors Lizard Spock\n"
            "===================\n"
            "1) ✊ (Rock)\n"
            "2) ✋ (Paper)\n"
            "3) ✌️ (Scissors)\n"
            "4) 🦎 (Lizard)\n"
            "5) 🖖 (Spock)\n"
        )

        try:
            player = int(input("Pick a number: "))
            if player not in [1, 2, 3, 4, 5]:
                print("Invalid input. Please choose 1, 2, 3, 4 or 5.\n")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        computer = random.randint(1, 5)
        choices = {1: "✊", 2: "✋", 3: "✌️", 4: "🦎", 5: "🖖"}

        print(f'Player chose: {choices[player]}')
        print(f'CPU chose: {choices[computer]}')

        if player == computer:
            print("It's a tie!\n")
        elif (player == 1 and computer == 3) or \
                (player == 2 and computer == 1) or \
                (player == 3 and computer == 2) or \
                (player == 1 and computer == 4) or \
                (player == 4 and computer == 5) or \
                (player == 5 and computer == 3) or \
                (player == 3 and computer == 4) or \
                (player == 4 and computer == 2) or \
                (player == 2 and computer == 5) or \
                (player == 5 and computer == 1):
            print("The player won!\n")
        else:
            print("The CPU won!\n")

        answer = input("Stop game? (yes/y to stop, no/n to continue, switch/s to switch game): ").strip().lower()
        if answer == "yes" or answer == "y":
            break
        elif answer == "switch" or answer == "s":
            rock_paper_scissors()
            break


if __name__ == "__main__":
    print(
        "What game do you want to play? \n"
        "1) Rock, Paper, Scissors\n"
        "2) Rock, Paper, Scissors, Lizard, Spock\n"
    )
    decision = int(input("Pick a game: "))
    if decision == 1:
        rock_paper_scissors()
    elif decision == 2:
        rock_paper_scissors_lizard_spock()
    else:
        print("Invalid input. Please choose 1, 2, or 3.\n")