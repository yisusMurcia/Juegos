startedBoard= [0 for i in range(0, 49)]
for i in range(1, 4):
    startedBoard[i*7+i]= 1
def seeBoard(board):
    for i in range(0, 7):
        line= []
        for j in range(0, 7):
            if board[(6-i)*7+j]== 1:
               line.append("o")
            elif board[(6-i)*7+j]== -1:
                line.append("x")
            else:
                line.append(" ")
        print(line)
    nums= [str(i) for i in range(1, 8)]
    print(nums)
def player(board, num=-1):
    column= input("Select a column")
    if column in "1234567":
        column= int(column)-1
        for i in range(0, 7):
            if board[column+7*i] == 0:
                board[column+7*i]= num
                return board

def tie(board):
    if 0 in board:
        return False
    else:
        return True

def win(board):
    for i in range (0, 7):
        count= 0
        #vertical
        if board[21+i]!= 0:
            for j in range(0, 7):
                if board[j*7+i]== board[21+i]:
                    count+=1
                    if count==3:
                        return True
                else:
                    count= 0
        for j in range(0, 7):
            #horizontal
            if board[7*i+3]== 0:
                break
            if  j==3:
                continue
            if board[i*7+j]== board[i*7+3]:
                count+=1
                if count==3:
                    return True
            else:
                count= 0
    #diagonal
    diagonalPoints= [
        [21, 3],
        [21, 45],
        [27, 3],
        [27, 45],
        [22, 10],
        [22, 38],
        [26, 10],
        [26, 38],
        [23, 17],
        [23, 31],
        [25, 17],
        [25, 31],
        [24, 24]
    ]
    player= 0
    potentialDiagonal= False
    for points in diagonalPoints:
        if board[points[0]]==0:
            continue
        if board[points[0]]== board[points[1]]:
            player= board[points[0]]
            potentialDiagonal= True
        if potentialDiagonal:
            pointsDistances= [8, 6]
            for disntance in pointsDistances:
                count= 0
                i= points[0]
                while board[i]== player and i>= 0:
                    i-=disntance
                #Restaurar el inicio de la conexión
                #Restore the start of the connection
                i+= disntance
                while i <49:
                    if board[i]== player:
                        count+= 1
                        if count==4:
                            return True
                    else:
                        count= 0
                        break
                    i+= disntance
    return False

board= startedBoard[:]
seeBoard(board)
turn= 1
while not tie(board):
    board= player(board, turn)
    turn*=-1
    seeBoard(board)
    if win(board):
        print("game over")
        break