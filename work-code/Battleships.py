import random
import time

# Function to display the start menu
def start_menu():
    print("-" * 45)
    print("""

        
             !!!     Welcome to Battleships Game     !!!


        ⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⡇⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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
    print("-" * 45)
    print("1. Play Game")
    print("2. View Highscores")
    print("3. Exit")
    print("-" * 45)

# Function to print the game board
def print_board(board):
    print("""

                          1    2    3    4    5    6    7    8
                         ____ ____ ____ ____ ____ ____ ____ ____                
                        |    |    |    |    |    |    |    |    |                
                     A  |    |    |    |    |    |    |    |    |                   
                        |____|____|____|____|____|____|____|____|              
                        |    |    |    |    |    |    |    |    |
                     B  |    |    |    |    |    |    |    |    |
                        |____|____|____|____|____|____|____|____|
                        |    |    |    |    |    |    |    |    |
                     C  |    |    |    |    |    |    |    |    |
                        |____|____|____|____|____|____|____|____|
                        |    |    |    |    |    |    |    |    |
                     D  |    |    |    |    |    |    |    |    |
                        |____|____|____|____|____|____|____|____|
                        |    |    |    |    |    |    |    |    |
                     E  |    |    |    |    |    |    |    |    |
                        |____|____|____|____|____|____|____|____|
                        |    |    |    |    |    |    |    |    |
                     F  |    |    |    |    |    |    |    |    |
                        |____|____|____|____|____|____|____|____|
                        |    |    |    |    |    |    |    |    |
                     G  |    |    |    |    |    |    |    |    |
                        |____|____|____|____|____|____|____|____|

                        """)
    
    for i in range(0, len(board), 4):
        print("+".join(board[i:i + 4]))

def save_highscores(score):
    with open("highscores battleships.txt, "a") as file:
        file.write(f"{scores}\n")


def view_highscores():
    print("Highscores:")
    try:
        with open("highscores battleships.txt", "r") as file:
            highscores = file.readlines()
            if not highscores:
                print("There is no highscores saved yet.")
            else:
                for idx, score in enumerate(highscores, start=1):
                    print(f"{idx}. {int(score)}")
    except FileNotFoundError:
        print("There is no highscores saved yet.")

# Function to play the game
def play_game():
    score = 0  # Initialize the score
    # Mapping between chess coordinates and index values
    chess_coordinates = {
        'A1': 0, 'A2': 1, 'A3': 2, 'A4': 3,
        'B1': 4, 'B2': 5, 'B3': 6, 'B4': 7,
        'C1': 8, 'C2': 9, 'C3': 10, 'C4': 11,
        'D1': 12, 'D2': 13, 'D3': 14, 'D4': 15
    }

    # Initialize the game board with '*' representing sea
    board = ["--*--"] * 16
    print_board(board)

    # Place 4 ships randomly on the board
    for i in range(4):
        ship = random.choice(list(chess_coordinates.values()))
        board[ship] = ""

    # Display the board with ships
    print_board(board)
    screen_board = board.copy()

    # Allow the player to make 5 guesses
    for i in range(5):
        print("-" * 45)
        print("", str(5 - i))

        # Get the player's guess and convert it to an index value
        while True:
            try:
                guess = input(
                    """
                       
                          1    2    3    4    5    6    7    8
                         ____ ____ ____ ____ ____ ____ ____ ____                
                        |    |    |    |    |    |    |    |    |                
                     A  |    |    |    |    |    |    |    |    |                   
                        |____|____|____|____|____|____|____|____|              
                        |    |    |    |    |    |    |    |    |
                     B  |    |    |    |    |    |    |    |    |
                        |____|____|____|____|____|____|____|____|
                        |    |    |    |    |    |    |    |    |
                     C  |    |    |    |    |    |    |    |    |
                        |____|____|____|____|____|____|____|____|
                        |    |    |    |    |    |    |    |    |
                     D  |    |    |    |    |    |    |    |    |
                        |____|____|____|____|____|____|____|____|
                        |    |    |    |    |    |    |    |    |
                     E  |    |    |    |    |    |    |    |    |
                        |____|____|____|____|____|____|____|____|
                        |    |    |    |    |    |    |    |    |
                     F  |    |    |    |    |    |    |    |    |
                        |____|____|____|____|____|____|____|____|
                        |    |    |    |    |    |    |    |    |
                     G  |    |    |    |    |    |    |    |    |
                        |____|____|____|____|____|____|____|____|
                        

                

                    Where should we bomb, commander!? (Enter coordinates, e.g., A1): """
                )
                # Convert chess coordinate to index value
                guess_index = chess_coordinates.get(guess.upper())

                if guess_index is not None:
                    break
                else:
                    print("Invalid input. Please enter a valid chess coordinate.")
            except ValueError:
                print("Invalid input. Please enter a valid chess coordinate.")

        # Check if the guess hits a ship and update the score
        if board[guess_index] == "":
            print("We hit them !!!")
            screen_board[guess_index] = "--H--"
            score += 1
        else:
            print("That was close but not enough !!!")
            screen_board[guess_index] = "--X--"

        # Display the updated board
        print_board(screen_board)
        time.sleep(2)

    # Check if all ships are sunk and display the result
    if screen_board.count("--H--") == 4:
        print("They became food for fish")
    else:
        print("We lost the war :(")

    # Print the final score
    print(f"Your score: {score}")
    print("GAME OVER")

# Main function to run the game
def main():
    while True:
        start_menu()
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            play_game()
        elif choice =="2":

        elif choice == "3":
            print("Exiting game")
            break
        else:
            print("Invalid choice. Enter 1 to play and 2 to exit.")

# Entry point of the program
if __name__ == "__main__":
    main()

# Print GAME OVER after exiting the game
print("GAME OVER"))

