# ------- Global Variables ---------

# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game is still going
game_playing = True

# Who won? Or Tie?
winner = None

# Whose turn is it
current_player = "X"


# -------- Functions ----------------

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():

    display_board()

    while game_playing:

        handle_turn()

        check_if_game_over()

        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won, step it up!")
    elif winner == None:
        print("Tie")

# Handle a single turn for either player


def handle_turn():

    # Get position from player
    print(current_player + "'s turn.")
    position = input("Choose a posiiton from 1-9: ")

    # Whatever user inputs, makes sure its valid and space is open
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a posiiton from 1-9: ")

        # Get correct index on the board
        position = int(position) - 1

        # Make sure spot is open on board
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    board[position] = current_player

    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    # Set up global variables
    global winner

    #  Check Rows
    row_winner = check_rows()
    # Check Columns
    column_winner = check_columns()
    # Check Diagonal
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        # there was no win
        winner = None
    return None


def check_rows():

    # Set up global variables
    global game_playing

    # Check if rows have same value (and isnt empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If any row has a match, flag for a win
    if row_1 or row_2 or row_3:
        game_playing = False

    # Return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return None


def check_columns():
    # Set up global variables
    global game_playing

    # Check if columns have same value (and isnt empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # If any column has a match, flag for a win
    if column_1 or column_2 or column_3:
        game_playing = False

    # Return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return None


def check_diagonals():
    # Set up global variables
    global game_playing

    # Check if diagonal have same value (and isnt empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    # If any diagonal has a match, flag for a win
    if diagonal_1 or diagonal_2:
        game_playing = False

    # Return the winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return None

# Check if there is a Tie


def check_if_tie():

    # set global variables
    global game_playing

    # If board is full
    if "-" not in board:
        game_playing = False
        return True

    # Else there is no tie
    else:
        return False


def flip_player():
    # global variables we need
    global current_player

    # If current player was X, then change it to O
    if current_player == "X":
        current_player = "O"
    # IF current player was O, then change it to X
    elif current_player == "O":
        current_player = "X"
    return None


play_game()
