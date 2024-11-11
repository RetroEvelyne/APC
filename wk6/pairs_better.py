from random import shuffle
from os import system
import sys

class Color:
    red = "\033[91m"
    green = "\033[92m"
    yellow = "\033[93m"
    blue = "\033[94m"
    purple = "\033[95m"
    cyan = "\033[96m"
    norm = "\033[0m"
    
    @staticmethod
    def print_error(msg):
        print(f"{Color.red}{msg}{Color.norm}")

def print_help():
    print_title()
    print(f"\n{Color.blue}Memory Game {Color.cyan}-{Color.blue} A tui Concentration style card game")
    print(f"\n{Color.blue}Optional arguments:")
    print(f"  {Color.blue}├─>{Color.purple}   help{Color.blue}   ─> Prints this message")
    print(f"  {Color.blue}╰─>{Color.purple} [number]{Color.blue} ─> The deck multiplier you want to use")
    print(f"\n{Color.blue}Press any key to quit...")

def print_title():
    system("clear")
    print(" "*10 + f"{Color.cyan}------------{Color.norm}")
    print(" "*10 + f"{Color.blue}Memory Game!{Color.norm}")
    print(" "*10 + f"{Color.cyan}------------{Color.norm}")


def show_cards(cards, revealed, moves):
    print_title()
    print(f"{Color.blue}Moves: {Color.purple}{moves}{Color.norm}")
    print(f"\n{Color.blue}Cards:{Color.norm}", end=" ")
    
    for card_index in range(len(cards)):
        if revealed[card_index]:
            print(Color.red + cards[card_index] + Color.norm, end=" ")
        else:
            print(Color.purple + f"{card_index}" + Color.norm, end=" ")

    print("\n")

def get_input(revealed, first_choice=None):
    while True:
        choice = input(f"{Color.blue}What is your choice ({Color.purple}0-7 / q{Color.blue})?\n╰─> {Color.norm}") 
        if choice == "q":
            print_title()
            input("\n" + " "*10 + f"{Color.blue}Ok, Goodbye!")
            system("clear")
            exit()
        try:
            choice = int(choice)
            if first_choice is not None:
                if first_choice == choice:
                    Color.print_error("Please do not choose the same number twice")
                    continue
            if 0 <= choice <= len(revealed)-1:
                if not revealed[choice]:
                    return choice
                else:
                    Color.print_error("Already revealed")
            else: Color.print_error("Please input a correct value")
        except ValueError:
            Color.print_error("Please at least input a number come on man")

def gen_deck(size_multiplier=1):
    cards = ["♠", "♠", "♥", "♥", "♦", "♦", "♣", "♣"] * size_multiplier
    shuffle(cards)
    return cards

def main():
    if len(sys.argv) >= 2:
        try:
            cards = gen_deck(int(sys.argv[1]))
        except ValueError:
            print_title()
            Color.print_error("\nInvalid deck multiplier passed, assuming no multiplier")
            cards = gen_deck()
            input()
    else:
        cards = gen_deck()

    revealed = [False for _ in range(len(cards))]
    moves = 0
    pairs_found = 0

    while pairs_found < len(cards)/2:
        show_cards(cards, revealed, moves)

        choice1 = get_input(revealed)
        revealed[choice1] = True
        show_cards(cards, revealed, moves)

        choice2 = get_input(revealed, choice1)
        revealed[choice2] = True
        show_cards(cards, revealed, moves)

        moves += 1

        if cards[choice1] == cards[choice2]:
            print(" "*11 + f"{Color.red}Match found!{Color.norm}")
            pairs_found += 1
        else:
            Color.print_error(" "*13 + "No match!")
            revealed[choice1] = revealed[choice2] = False
        input(f"{Color.blue}Press Enter to continue...{Color.norm}")

    print_title()
    print(f"\n{Color.blue}Congratulations! You won in {Color.purple}{moves}{Color.blue} moves!{Color.norm}")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        print()
        if sys.argv[1] == "help":
            print_help()
            system("read -n1 -r")
            system("clear")
            exit()
    main()

