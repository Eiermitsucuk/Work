import random
import time

def start_menu():
    print("""
        
             !!!     Welcome to Battleships Game     !!!

             ⠀⠀  ⠀⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⡇⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡇⠀⠀⠀⠀⠀⠀⠀⣀⡤⡞⢫⡎⢸⢱⠀⠀⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣟⡒⣶⣶⣶⣾⡯⠟⠛⠁⠈⢳⣼⣸⠀⠀⠀⠈⠣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠉⠓⠿⣟⣓⣒⣀⡤⠶⠚⠉⢹⣿⠀⠀⠀⠀⠀⠘⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣟⣿⢿⣶⡗⠒⠒⠒⠒⠲⠶⣶⠶⠶⠦⠼⢿⣦⣀⣀⣀⣀⣀⠀⠀⠈⠳⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⣄⠀⠀⠀⠀⠀⠈⢣⡀⠀⠀⠀⠈⠳⣌⠉⠉⠉⠉⠙⢿⡷⠿⢶⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠝⢆⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠙⢦⡀⠙⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⢧⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠙⢆⠀⠀⠀⠀⠈⢳⡀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⣧⠀⠀⠀⠀⠀⠀⠈⢣⠀⠀⠀⠀⠀⠈⣦⠀⠀⠀⠀⠀⠹⡀⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡆⠀⠀⠀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⢻⡄⠀⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⢸⠀⠀⠀⠀⠀⠀⠸⣦⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠈⢧⠀⠀⠀⠈⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠘⡆⠀⡆⠀⠀⠀⠀⡟⡇⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⢸⣆⠀⠀⠀⠀⠹⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⡇⡀⢰⠀⠀⠀⠀⣷⠃⡇⢠⡄⠀⠀⢸⢸⢠⡄⠀⠘⡟⣿⠀⠀⠀⠀⠀⢸⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠟⡿⠀⢸⢀⢀⠀⢠⡟⡔⡇⡌⡇⠀⠀⣺⢸⢸⣿⣰⢀⣧⡿⠀⠀⠀⣀⣴⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣤⣤⠤⢤⣤⣾⠀⡇⡀⡌⣼⣼⠀⣴⣿⡇⡇⣿⡇⡆⣀⣿⣿⣸⢹⣿⢸⣿⠀⢰⠒⠾⣿⣻⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⡞⠛⣻⣿⣟⡛⠛⣻⡇⢸⢁⣿⡇⣿⣇⣤⣿⣿⢳⣿⢻⢳⣿⣹⣏⡇⣯⣿⠃⣼⣾⡤⢾⠁⠈⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⣾⣷⣲⣾⣿⣶⣾⢁⡞⣾⣾⣻⣿⣽⣿⠟⣏⣎⡟⣞⣾⣿⣿⢹⣼⣹⣿⣴⠟⠉⠀⣾⠀⢰⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⢯⣿⣿⣿⣻⣿⠃⡼⣹⢳⣿⣿⣽⣿⣿⣾⡘⣹⣽⣻⡿⣿⣣⣷⡿⠛⢻⡾⠷⣄⢀⣿⠀⢸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡷⠶⠯⠿⣭⡾⢃⡞⣱⢟⣿⣿⣿⣻⣤⣤⣽⣿⡷⣧⣽⡿⢟⣉⡁⠀⠀⢨⢿⣶⣿⣿⠇⢀⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣤⣼⣷⣤⣤⣼⣿⣗⣾⣤⣽⣊⣿⣿⣿⣿⢯⡤⠿⣿⣿⣿⡼⠷⠈⢃⣠⣤⣶⣿⣿⣿⢿⣿⠀⣸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣍⠉⢹⣿⡿⣿⣿⠿⠿⠛⠛⢹⣯⢹⣿⡟⣆⢸⠿⣠⣿⣿⣻⠧⠖⠛⣿⠖⠋⣽⣿⢽⣶⣿⠣⣶⣿⠃⠀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣷⣼⣿⣷⣿⣿⣶⣄⣀⣀⣀⣠⣤⣿⣿⠛⠿⠿⣛⣻⡷⠋⠀⠐⠀⣿⣶⢾⣿⠟⣫⢴⠏⢠⣿⢻⣧⣴⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣤⣀⠀⠀⢀⣀⡉⠉⠉⠛⢛⣛⣿⠿⣿⣶⣾⣿⣩⣅⡤⠶⠶⠛⠉⠙⠛⣿⣛⣭⠏⢠⣿⠻⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢻⣟⡛⠛⠓⠒⠲⠲⠾⠿⠿⠿⠿⠛⠛⠛⠛⠛⠉⠁⠀⣀⣀⣠⣴⣞⡿⢽⣿⠃⣰⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⠹⣿⡦⣄⣠⣠⣦⣤⣀⣀⣀⣀⣀⣀⣀⣤⣤⡤⠤⠶⠿⠛⣋⣿⣷⣶⡿⡥⣶⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡿⠋⣼⠿⣻⡿⣿⣻⣟⣦⣄⣀⣠⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣲⣾⣿⣟⣿⣿⠋⣠⣾⠯⢤⣄⡀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣁⢸⡇⠈⣇⠀⣿⠛⣦⠙⢪⣷⠿⠛⠓⠒⠾⠷⣶⡶⠶⠶⢶⣶⣶⣶⣶⣟⣹⣯⣷⠞⢁⣴⠿⢿⡶⣄⡉⠟⣿⡍⠉⣙⡻⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢿⢿⠇⢿⣄⠘⠳⠽⠷⢯⡀⢹⣇⠀⠀⣀⡤⠤⠤⢤⣈⡛⢶⣞⠁⢀⣀⠀⠉⠻⠟⠡⠴⠛⠛⠛⠋⠛⢳⣍⠀⠹⣿⡄⠈⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⣶⣤⣤⣼⠇⠈⠻⣦⣀⢹⣷⣶⠀⠀⠈⠉⠛⢿⣦⣼⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣏⢀⣾⡿⠣⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀
        """)
    print("1. Play Game")
    print("2. View Highscores")
    print("3. Exit")
    print("-" * 45)

def create_board(rows, columns):
    return [[' ' for _ in range(columns)] for _ in range(rows)]

def print_board(board):
    rows = len(board)
    columns = len(board[0])

    print("  " + " ".join([chr(ord('A') + i) for i in range(columns)]))

    for i, row in enumerate(board):
        print(f"{i} {' '.join(row)}")

def letter_to_index(letter):
    return ord(letter) - ord('A')

def save_highscores(score):
    with open("battleships_highscores.txt", "a") as file:
        file.write(f"{score}\n")

def view_highscores():
    print("Highscores:")
    try:
        with open("battleships_highscores.txt", "r") as file:
            highscores = file.readlines()
            if not highscores:
                print("There is no highscores saved yet.")
            else:
                for idx, score in enumerate(highscores, start=1):
                    print(f"{idx}. {int(score)}")
    except FileNotFoundError:
        print("There is no highscores saved yet.")

def play_game():
    score = 0

    # Create the game board
    rows = 5
    columns = 5
    board = create_board(rows, columns)

    for i in range(4):
        ship_row = random.randint(0, len(board) - 1)
        ship_col = random.randint(0, len(board[0]) - 1)
        board[ship_row][ship_col] = '0'

    print_board(board)
    screen_board = [[' ' for _ in range(len(board[0]))] for _ in range(len(board))]

    for i in range(5):
        print("-" * 45)
        print("", str(5 - i))

        while True:
            try:
                guess = input(" Where should we bomb, commander!? (Enter coordinates, e.g., A1): ")
                guess_index = letter_to_index(guess[0]), int(guess[1])

                if 0 <= guess_index[0] < len(board) and 0 <= guess_index[1] < len(board[0]):
                    break
                else:
                    print("Invalid input. Please enter valid coordinates.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid coordinates.")

        if board[guess_index[0]][guess_index[1]] == '0':
            print("We hit them !!!")
            screen_board[guess_index[0]][guess_index[1]] = "H"
            score += 1
        else:
            print("That was close but not enough !!!")
            screen_board[guess_index[0]][guess_index[1]] = "X"

        print_board(screen_board)
        time.sleep(2)

    if sum(row.count("H") for row in screen_board) == 4:
        print("They became food for fish")
    else:
        print("We lost the war :(")

    return score

def main():
    score = 0
    while True:
        start_menu()
        choice = input("Enter your choice (1, 2 or 3.): ")

        if choice == "1":
            score = play_game()
        elif choice == "2":
            view_highscores()
        elif choice == "3":
            print("Exiting game")
            break
        else:
            print("Invalid choice. Enter 1 to play, 2 to view highscores and 3 to exit.")

    print(f"Your score: {score}")
    save_highscores(score)
    print("GAME OVER")

if __name__ == "__main__":
    main()
