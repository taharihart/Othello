def init_board(n):
    table = []
    index = (n / 2) - 1
    for i in range(n):
        inner = []
        if i == index:
            for j in range(n):
                inner.append('-')
            for a in range(n):
                if a == index:
                    inner[a] = 'W'
                    inner[a + 1] = 'B'
        elif i == index + 1:
            for j in range(n):
                inner.append('-')
            for a in range(n):
                if a == index:
                    inner[a] = 'B'
                    inner[a + 1] = 'W'
        else:
            for k in range(n):
                inner.append('-')
        table.append(inner)
    return table

def get_possible_positions(board,player,opponent):
    res = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == '-':
                if j > 1 and board[i][j - 1] == opponent and check_surrounding(board, i, j,
                                                                               player):  # check left neighbour
                    rep = 2
                    for a in range(j - 2, -1, -1):
                        if board[i][a] == player:
                            res.append((i, j, rep))
                            break
                        rep += 1
                if j < len(board) - 2 and board[i][j + 1] == opponent and check_surrounding(board, i, j,
                                                                                            player):  # check right neighbour
                    rep = 2
                    for a in range(j + 2, len(board)):
                        if board[i][a] == player:
                            res.append((i, j, rep))
                            break
                        rep += 1
                if i > 1 and board[i - 1][j] == opponent and check_surrounding(board, i, j,
                                                                               player):  # check top neighbour
                    rep = 2
                    for a in range(i - 2, -1, -1):
                        if board[a][j] == player:
                            res.append((i, j, rep))
                            break
                        rep += 1
                if i < len(board) - 2 and board[i + 1][j] == opponent and check_surrounding(board, i, j,
                                                                                            player):  # check bottom neighbour
                    rep = 2
                    for a in range(i + 2, len(board)):
                        if board[a][j] == player:
                            res.append((i, j, rep))
                            break
                        rep += 1
                if i > 1 and j < len(board) - 2 and board[i - 1][j + 1] == opponent and check_surrounding(board, i, j,
                                                                                                          player):  # check diagonal up right side
                    rep = 2
                    c = j + 2
                    for a in range(i - 2, -1, -1):
                        if c < len(board) and board[a][c] == player:
                            res.append((i, j, rep))
                            break
                        rep += 1
                        c += 1

                if i > 1 and j > 1 and board[i - 1][j - 1] == opponent and check_surrounding(board, i, j,
                                                                                             player):  # check diagonal left up side
                    rep = 2
                    c = j - 2
                    for a in range(i - 2, -1, -1):
                        if c >= 0 and board[a][c] == player:
                            res.append((i, j, rep))
                            break
                        rep += 1
                        c -= 1

                if i < len(board) - 2 and j < len(board) - 2 and board[i + 1][j + 1] == opponent and check_surrounding(
                        board, i, j, player):  # check diagonal right down side
                    rep = 2
                    c = j + 2
                    for a in range(i + 2, len(board)):
                        if c < len(board) and board[a][c] == player:
                            res.append((i, j, rep))
                            break
                        rep += 1
                        c += 1

                if i < len(board) - 2 and j > 1 and board[i + 1][j - 1] == opponent and check_surrounding(board, i, j,
                                                                                                          player):  # check diagonal left down side
                    rep = 2
                    c = j - 2
                    for a in range(i + 2, len(board)):
                        if c >= 0 and board[a][c] == player:
                            res.append((i, j, rep))
                            break
                        rep += 1
                        c -= 1
    same_lst = []
    for i in range(len(res) - 1):
        if res[i][0] == res[i + 1][0] and res[i][1] == res[i + 1][1]:
            same_lst.append((i, i + 1))
    for same in same_lst:
        if res[same[0]][2] > res[same[1]][2]:
            res.remove(res[same[1]])
        else:
            res.remove(res[same[0]])
    return res

def update_board(board,row,col,player):
    if check_position(board,row,col) == True:
        if check_surrounding(board,row,col,player) == True:
            if change_piece(board,row,col,player) == True:
                return True
    return False

def check_position(board,row,col):
    if board[row][col] == '-':
        return True
    else:
        return False

def check_surrounding(board,row,col,player):
    if col>0: # check left neighbour
        if board[row][col-1] == player:
            return False
    if col<len(board)-1: #check right neighbour
        if board[row][col+1] == player:
            return False
    if row>0: #check top neighbour
        if board[row-1][col] == player:
            return False
    if row<len(board)-1: #check bottom neighbour
        if board[row+1][col] == player:
            return False
    return True

def change_piece(board,row,col,player):
    return_value = False
    if col < len(board) - 2 and board[row][col + 1] != '-':  # change right side
        for i in range(col, len(board) - 2):
            if board[row][i + 2] == player:
                for j in range(col, i + 2):
                    board[row][j] = player
                return_value = True
                break

    if col > 1 and board[row][col - 1] != '-':  # change left side
        for i in range(col, 1, -1):
            if board[row][i - 2] == player:
                for j in range(col, i - 2, -1):
                    board[row][j] = player
                return_value = True
                break

    if row > 1 and board[row - 1][col] != '-':  # change top side
        for i in range(row, 1, -1):
            if board[i - 2][col] == player:
                for j in range(row, i - 2, -1):
                    board[j][col] = player
                return_value = True
                break

    if row < len(board)-2 and board[row+1][col] != '-':# change bottom side
        for i in range(row,len(board)-2):
            if board[i+2][col] == player:
                for j in range(row,i+2):
                    board[j][col] = player
                return_value = True
                break

    if row > 1 and col < len(board)-2 and board[row-1][col+1] != '-' and board[row-1][col+1] != player: #change diagonal up right side
        a = col
        for i in range(row,1,-1):
            if board[i-2][a+2] == player:
                a = col
                for j in range(row,i-2,-1):
                    board[j][a] = player
                    a += 1
                return_value = True
                break
            a += 1

    if row > 1 and col > 1 and board[row-1][col-1] != '-' and board[row-1][col-1] != player: # change diagonal left up side
        a = col
        for i in range(row, 1, -1):
            if board[i - 2][a - 2] == player:
                a = col
                for j in range(row, i - 2, -1):
                    board[j][a] = player
                    a -= 1
                return_value = True
                break
            a -= 1

    if row < len(board)-2 and col < len(board)-2 and board[row+1][col+1] != '-' and board[row+1][col+1] != player: # change diagonal right down side
        a = col
        for i in range(row,len(board)-2):
            if board[i + 2][a + 2] == player:
                a = col
                for j in range(row, i + 2):
                    board[j][a] = player
                    a += 1
                return_value = True
                break
            a += 1

    if row < len(board)-2 and col>1 and board[row+1][col-1] != '-' and board[row+1][col-1] != player: # change diagonal left down side
        a = col
        for i in range(row, len(board) - 2):
            if board[i + 2][a - 2] == player:
                a = col
                for j in range(row, i + 2):
                    board[j][a] = player
                    a -= 1
                return_value = True
                break
            a -= 1

    return return_value

def print_board(board):
    for line in board:
        print('----' * len(line) + '-')
        print('|', end=' ')
        print(' | '.join(line) + ' |')
    print('----' * len(line) + '-')
def game_over(board):
    if is_filled(board) or (len(get_possible_positions(board,'W','B')) == 0 and len(get_possible_positions(board,'B','W')) == 0):
        return True
    return False
def is_filled(board):
    for line in board:
        for inner in line:
            if inner == '-':
                return False
    return True
board = [['-', 'B', 'W', '-'],
         ['W', 'B', 'B', '-'],
         ['-', 'B', 'B', '-'],
         ['-', '-', '-', 'B']]
print(game_over(board))
print(get_possible_positions(board,'B','W'))
print(get_possible_positions(board,'W','B'))