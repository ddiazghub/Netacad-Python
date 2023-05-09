def is_valid(sudoku_board):

    sudoku_board = sudoku_board.split('\n')
    for row in range(len(sudoku_board)):
        for i in range(len(sudoku_board[row]) - 1):
            for j in range(int(sudoku_board[row][i + 1]), len(sudoku_board[row])):
                if sudoku_board[row][i] == sudoku_board[row][j]:
                    return False
                
                if sudoku_board[i][row] == sudoku_board[j][row]:
                    return False

    for i in range(0, len(sudoku_board), 3):
        for j in range(0, len(sudoku_board), 3):
            rows_3 = sudoku_board[i: i + 3]
            for row in rows_3:
                row = rows_3[j: j + 3]
            rows_3 = ''.join(rows_3)
            for k in range(len(rows_3) - 1):
                for l in range(k + 1, len(rows_3)):
                    if rows_3[k] == rows_3[l]:
                        return False
    return True

stre = '''295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672'''
print(is_valid(stre))
        
