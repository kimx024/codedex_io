import random
"""
This script allows the user to play the classic game Rock, Paper Scissors
There is also a variant included called Rock, Paper, Scissors, Lizard, Spock.
This variant has been made popular through the "The Big Bang Theory".

This script is part of my (@milakim) Codédex checkpoint project of the beginner Python course.
"""

# First function: classic Rock Paper Scissors
def rock_paper_scissors():
    # Exact a while loop to play the game as long as the user doesn't stop
    while True:
        print(
            "===================\n"
            "Rock Paper Scissors\n"
            "===================\n"
            "1) ✊ (Rock)\n"
            "2) ✋ (Paper)\n"
            "3) ✌️ (Scissors)\n"
        )

        # Pick a number for the player and pick a random number for the computer
        try:
            player = int(input("Pick a number: "))
            if player not in [1, 2, 3]:
                print("Invalid input. Please choose 1, 2, or 3.\n")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        # Display these values by converting them to emojis again for better readability
        computer = random.randint(1, 3)
        choices = {1: "✊", 2: "✋", 3: "✌️"}

        print(f'Player chose: {choices[player]}')
        print(f'CPU chose: {choices[computer]}')

        # Decide if it's a tie or if there is a winner according to the rules:
        # - Rock beats Scissors
        # - Scissors beats Paper
        # - Paper beats Rock

        if player == computer:
            print("It's a tie!\n")
        elif (player == 1 and computer == 3) or \
                (player == 2 and computer == 1) or \
                (player == 3 and computer == 2):
            print("The player won!\n")
        else:
            print("The CPU won!\n")

        # Allow for a switching mechanism to the other variant, play again and activate the while loop again
        # or stop the loop.
        answer = input("Stop game? (yes/y to stop, no/n to continue, switch/s to switch game): ").strip().lower()
        if answer == "yes" or answer == "y":
            break
        elif answer == "switch" or answer == "s":
            rock_paper_scissors_lizard_spock()
            break


# Second function: Rock, Paper, Scissors, Lizard, Spock
def rock_paper_scissors_lizard_spock():
    # Exact almost the same while loop as the first function to play the game as long as the user doesn't stop
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

        # Pick a number for the player and pick a random number for the computer. Elaborated for more options
        try:
            player = int(input("Pick a number: "))
            if player not in [1, 2, 3, 4, 5]:
                print("Invalid input. Please choose 1, 2, 3, 4 or 5.\n")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        # Display these values by converting them to emojis again for better readability
        computer = random.randint(1, 5)
        choices = {1: "✊", 2: "✋", 3: "✌️", 4: "🦎", 5: "🖖"}

        print(f'Player chose: {choices[player]}')
        print(f'CPU chose: {choices[computer]}')

        # Decide if it's a tie or if there is a winner according to the rules:
        # - Rock beats Scissors and Lizard
        # - Scissors beats Paper and beats Spock
        # - Paper beats Rock and Lizard
        # - Lizard beats Spock and beats Paper
        # - Spock beats Rock and Scissors
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

        # Allow for a switching mechanism to the other variant, play again again and activate the while loop again
        # or stop the loop.
        answer = input("Stop game? (yes/y to stop, no/n to continue, switch/s to switch game): ").strip().lower()
        if answer == "yes" or answer == "y":
            break
        elif answer == "switch" or answer == "s":
            rock_paper_scissors()
            break


# Main function to execute both functions written as above
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