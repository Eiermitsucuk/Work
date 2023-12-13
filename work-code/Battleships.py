import random
import time

def start_menu():
    print("-"*45)
    print("Welcome to Battleships Game")
    print("-"*45)
    print("1. Play Game")
    print("2. Exit")
    print("-"*45)

def print_board(board):
    print("-"*45)
    for i in range(0, len(board), 4):
        print("+".join(board[i:i+4]))

def play_game():
    numbers = list(range(16))
    print(numbers)

    board = ["--*--"] * 16
    print_board(board)

    for i in range(4):
        ship = random.choice(numbers)
        numbers.remove(ship)
        board[ship] = "--A--"

    print_board(board)
    screen_board = board.copy()

    for i in range(5):
        print("-"*45)
        print("", str(5-i))

        while True:
            try:
                guess = int(input(
                    """

                    0-1-2-3
                    4-5-6-7
                    8-9-10-11
                    12-13-14-15

                    Where should we bomb, commander!? =
                    """))

                if 0 <= guess <= 15:
                    break
                else:
                    print("Please enter a number between 0 and 15.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if board[guess] == "--A--":
            print("We hit them !!!")
            screen_board[guess] = "--H--"
        else:
            print("That was close but not enough !!!")
            screen_board[guess] = "--X--"

        print_board(screen_board)
        time.sleep(3)

    if screen_board.count("--H--") == 4:
        print("They became food for fish")
    else:
        print("We lost the war :(")

    print("GAME OVER")

def main():
    while True:
        start_menu()
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            play_game()
        elif choice == "2":
            print("Exiting game")
            break
        else:
            print("Invalid choice. Enter 1 to play and 2 to exit.")

if __name__ == "__main__":
    main()

print("GAME OVER")
