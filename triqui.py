startingBoard= [0, 0, 0, 0, 0, 0, 0, 0, 0]
MAX= 1
MIN= -1

#Ordenar movimientos para minMax
def sortMovements(x):
    return x[0]

#Revisar los mejores movimientos
#Check best movements
def minmax(board, turn):
    global machineMove
    #El turno es 1 0 -1
    #The turn is 1 or -1
    movements= []
    if win(board)!= None:
        return [win(board)]
    for i in range(0, len(board)):
        if board[i]== 0:
            auxBoard= board[:]
            auxBoard[i]= turn
            puntation= minmax(auxBoard, turn*(-1))
            movements.append([puntation, i])
    if turn== MAX:
        movements.sort(key= sortMovements, reverse=True)
        movement= movements[0]
        machineMove= movement[1]
        return movement[0]
    else:
        movements.sort(key= sortMovements)
        movement= movements[0]
        return movement[0]
    
def seeBoard(board):
    for i in range(0, 3):
        squeares= [str(j+i*3+1) for j in range(0, 3)]
        line= []
        for j in range(0, 3):
            if (board[i*3+j]== -1):
                line.append("x")
            elif (board[i*3+j]==1):
                line.append("o")
            else:
                line.append(" ")
        print(squeares)
        print(line)

def player(board, num= -1):
    square=input("select the place from 1 to 9 or 0 to reset the game ")
    if square in "0123456789":
        square= int(square)
        if square== 0:
            board= startingBoard[:]
            return board
        square-= 1
        if len(str(square))==1:
            if board[square]==0:
                board[square]= num
                return board
    print("Something go wrong, try it again")
    seeBoard(board)
    return player(board, num)

def machinePlay(board):
    global machineMove
    punt= minmax(board, MAX)
    board[machineMove]= MAX
    return board

def tie(board):
    if not 0 in board:
        return True
    
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
            return board[line[0]]
    if tie(board):
        return 0
    else:
        return None
    
def play():
    loop= True
    while loop:
        twoPlayers= None
        while twoPlayers== None:
            numOfPlayers= input("1 or 2 players")
            if numOfPlayers in "12":
                twoPlayers= int(numOfPlayers)== 2
                print("Play for "+ str(numOfPlayers))
            else:
                print("Select 1 or 2")
        board= [0, 0, 0, 0, 0, 0, 0, 0, 0]
        turn1= True

        seeBoard(board)
        while 0 in board:
            if turn1:
                board= player(board)
                turn1= False
            else:
                if twoPlayers:
                    board= player(board, 1)
                else:
                    board= machinePlay(board)
                    print("Machine turne, moving: "+ str(machineMove+1))
                turn1= True
            seeBoard(board)
            if win(board)!= None:
                print("game over!")
                if win(board)==0:
                    print("tie")
                    break
                elif win(board)== MAX:
                    if twoPlayers:
                        winner= "player 2"
                    else:
                        winner= "Machine"
                else:
                    winner= "player"
                    if twoPlayers:
                        winner+= " 1"
                print ("winner: "+ str(winner))
                break
        again= input("For play again type 'yes'")
        if again!= "yes":
            loop= False
play()