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
    # Mapping between chess coordinates and index values
    chess_coordinates = {
        'A1': 0, 'A2': 1, 'A3': 2, 'A4': 3,
        'B1': 4, 'B2': 5, 'B3': 6, 'B4': 7,
        'C1': 8, 'C2': 9, 'C3': 10, 'C4': 11,
        'D1': 12, 'D2': 13, 'D3': 14, 'D4': 15
    }

    board = ["--*--"] * 16
    print_board(board)

    for i in range(4):
        ship = random.choice(list(chess_coordinates.values()))
        board[ship] = "--A--"

    print_board(board)
    screen_board = board.copy()

    for i in range(5):
        print("-"*45)
        print("", str(5-i))

        while True:
            try:
                guess = input(
                    """
                          A B C D
                        1 0 0 0 0
                        2 0 0 0 0
                        3 0 0 0 0
                        4 0 0 0 0

                    Where should we bomb, commander!? =
                    """)

                # Convert chess coordinate to index value
                guess_index = chess_coordinates.get(guess.upper())
                
                if guess_index is not None:
                    break
                else:
                    print("Invalid input. Please enter a valid chess coordinate.")
            except ValueError:
                print("Invalid input. Please enter a valid chess coordinate.")

        if board[guess_index] == "--A--":
            print("We hit them !!!")
            screen_board[guess_index] = "--H--"
        else:
            print("That was close but not enough !!!")
            screen_board[guess_index] = "--X--"

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

