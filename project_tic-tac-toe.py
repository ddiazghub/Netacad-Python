import random
import os


def display_board(board):
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|  ", row[0], "  |  ", row[1], "  |  ", row[2], "  |")
        print("|       |       |       |")
    
    print("+-------+-------+-------+")


def enter_move(board):
    move = int(input("Enter your move: "))
    free = make_list_of_free_fields(board)

    if move <= 3:
        move = (0, move - 1)
    elif move > 3 and move < 7:
        move = (1, move - 4)
    elif move > 6:
        move = (2, move - 7)
    
    if move in free:
        board[move[0]][move[1]] = "O"
    else:
        print("The field is occupied. Please input an empty field.")
        enter_move(board)


def make_list_of_free_fields(board):
    
    free = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] not in ("X", "O"):
                field = (i, j)
                free.append(field)
    
    return free


def victory_for(board, sign):
    6
    has_won = False
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] == sign:
            has_won = True
    
    for j in range(len(board[0])):
        if board[0][j] == board[1][j] == board[2][j] == sign:
            has_won = True

    if board[0][0] == board[1][1] == board[2][2] == sign or board[0][2] == board[1][1] == board[2][0] == sign:
        has_won = True

    return has_won


def draw_move(board):
    move = (random.randrange(4), random.randrange(4))
    free = make_list_of_free_fields(board)
    
    if move in free:
        board[move[0]][move[1]] = "X"
    else:
        draw_move(board)

print("WELCOME TO TIC-TAC-TOE!!!!")

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
while True:
    draw_move(board)
    display_board(board)
    
    if victory_for(board, "X"):
        print("You lose!")
        break

    if len(make_list_of_free_fields(board)) == 0:
        print("Tie!")
        break
    enter_move(board)
    display_board(board)

    if victory_for(board, "O"):
        print("You win!")
        break

    if len(make_list_of_free_fields(board)) == 0:
        print("Tie!")
        break

