import random

def show_cards(cards, revealed, moves):
    print("Memory Game!")
    print(f"Moves: {moves}")
    print("\nPositions:")
    
    for card_index in range(len(cards)):
        if revealed[card_index]:
            print(cards[card_index], end=" ")
        else:
            print(card_index, end=" ")

    print("\n")

def get_input(revealed, first_choice=None):
    while True:
        try:
            choice = int(input("What is your choice (0-7)? > ")) 
            if first_choice is not None:
                if first_choice == choice:
                    print("Please do not choose the same number twice")
                    continue
            if 0 <= choice <= 7:
                if not revealed[choice]:
                    return choice
                else:
                    print("Already revealed")
            else: print("Please input a correct value")
        except ValueError:
            print("Please at least input a number come on man")

def main():
    cards = ["A", "A", "B", "B", "C", "C", "D", "D"]
    random.shuffle(cards)

    revealed = [False for _ in range(8)]

    moves = 0

    pairs_found = 0

    while pairs_found < 4:
        show_cards(cards, revealed, moves)

        choice1 = get_input(revealed)
        revealed[choice1] = True
        show_cards(cards, revealed, moves)

        choice2 = get_input(revealed, choice1)
        revealed[choice2] = True
        show_cards(cards, revealed, moves)

        moves += 1

        if cards[choice1] == cards[choice2]:
            print("Match found!")
            pairs_found += 1
        else:
            print("No match!")
            revealed[choice1] = revealed[choice2] = False
        input("Press Enter to continue...")

    print(f"\nCongratulations! You won in {moves} moves!")
main()

