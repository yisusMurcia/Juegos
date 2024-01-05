startingBoard= [0, 0, 0, 0, 0, 0, 0, 0, 0]
def seeBoard(board):
    for i in range(0, 3):
        squeares= [str(j+i*3+1) for j in range(0, 3)]
        line= []
        for j in range(0, 3):
            if (board[i*3+j]== 1):
                line.append("x")
            elif (board[i*3+j]==-1):
                line.append("o")
            else:
                line.append(" ")
        print(squeares)
        print(line)
def player1(board):
    square=int(input("select the place from 1 to 9 or 0 to reset the game "))
    if square== 0:
        board= startingBoard[:]
        return board
    square-= 1
    if str(square) in "012345678" and len(str(square))==1:
        if board[square]==0:
            board[square]= 1
            return board
    print("Something go wrong, try it again")
    seeBoard(board)
    return player1(board)
def player2(board):
    square= int(input("select the place from 1 to 9 or 0 to reset the game "))
    if square== 0:
        board= startingBoard[:]
        return board
    square-= 1
    if str(square) in "012345678" and len(str(square))==1:
        if board[square]==0:
            board[square]= -1
            return board
        print("Something go wrong, try it again")
        seeBoard(board)
        return player2(board)
def win(board):
    lines= [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for line in lines:
        if board[line[0]]== board[line[1]] and board[line[2]]== board[line[0]] and board[line[0]]!=0:
            print("game over!")
            print ("winner: player "+ str(board[line[0]]))
            return True
play= True
board= [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn1= True
seeBoard(board)
while play and 0 in board:
    if turn1:
        board= player1(board)
        turn1= False
    else:
        board= player2(board)
        turn1= True
    seeBoard(board)
    if not 0 in board:
        print("tie")
    if win(board):
        play= False
        break