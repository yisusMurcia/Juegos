startedBoard= [0 for i in range(0, 49)]

def mark(board, turn, column):
    newBoard= board[:]
    for i in range(0, 7):
            num= column+7*i
            if num> 49:
                break
            elif board[num] == 0:
                newBoard[num]= turn
                break
    return newBoard

def evaluateBoard(board, player= 1):
    #Contar lineas posibles
    #Count possible lines
    count2= 0
    count3= 0
    count4= 0
    enemy= player*-1
    for i in range (0, 7):
        #vertical
        if board[21+i]!= enemy:
            count= 0
            num= 21+i
            while num>= 0 and board[num]!= enemy:
                num-= 7
            num+=7
            while num<=41+i:
                if board[num]!= player:
                    num+= 7
                    count+= 1
                else:
                    if count> 3:
                        count4+=1
                    break
            match count:
                    case 1:
                        break
                    case 2:
                        count2+= 1
                    case 3:
                        count3+=1
                    case _:
                        count4+= 1
        #horizontal
        if board[i*7+3]!= enemy:
            count= 0
            num= i*7+3
            while num>= i*7 and board[num]!= enemy:
                num-= 1
            num+=1
            while num< (i+1)*7:
                if board[num]!= enemy:
                    count+= 1
                    num+=1
                else:
                    if count> 3:
                        count4+=1
                    break
            match count:
                    case 1:
                        break
                    case 2:
                        count2+= 1
                    case 3:
                        count3+=1
                    case _:
                        count4+= 1
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
    for points in diagonalPoints:
        if board[points[0]]!= enemy and board[points[0]]== board[points[1]]:
            pointsDistances= [8, 6]
            for disntance in pointsDistances:
                count= 0
                i= points[0]
                while i>= 0 and board[i]!= enemy:
                    i-=disntance
                #Restaurar el inicio de la conexión
                #Restore the start of the connection
                i+= disntance
                while i <49:
                    if board[i]!= enemy:
                        count+= 1
                        i+= disntance
                    else:
                        if count> 3:
                            count4+=1
                        break
                match count:
                    case 1:
                        break
                    case 2:
                        count2+= 1
                    case 3:
                        count3+=1
                    case _:
                        count4+= 1
    return count2*2+ count3*9+ count4*100

def sortMovements(x):
    return x[0]

def minMax(board, turn, count= 0):
    global move
    if win(board):
        return 100*turn/count
    if  count== 6 or tie(board):
        return evaluateBoard(board, 1)- evaluateBoard(board, turn*-1)
    movements= []
    for i in range(0, 7):
        auxBoard= board[:]
        markedBoard= mark(auxBoard, turn, i)
        auxBoard= markedBoard
        puntuation= minMax(auxBoard, turn*-1, count+1)
        movements.append([puntuation, i])
    if turn== 1:
        movements.sort(key=sortMovements, reverse= True)
        movement= movements[0]
        move= movement[1]
        return movement[0]
    else:
        movements.sort(key=sortMovements)
        movement= movements[0]
        return movement[0]

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

def player(board, turn=-1):
    column= input("Select a column")
    if column in "1234567":
        column= int(column)-1
    marking= mark(board, turn, column)
    if marking== board:
        print("Something is wrong try again")
        return player(board, turn)
    else:
        board= marking
        return board

def tie(board):
    if 0 in board:
        return False
    else:
        return True

def win(board):
    for i in range (0, 7):
        #vertical
        if board[21+i]!= 0:
            count= 0
            player= board[21+i]
            num= 21+i
            while num>= 0 and board[num]== player:
                num-= 7
            num+=7
            while num< 49 and board[num]== player:
                num+= 7
                count+= 1
            if count== 4:
                return player
        #horizontal
        if board[i*7+3]!= 0:
            count= 0
            player= board[7*i+3]
            num= i*7+3
            while board[num]== player and num>= i*7:
                num-= 1
            num+=1
            while board[num]== player:
                count+= 1
                num+=1
            if count== 4:
                return player
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
                            return player
                    else:
                        count= 0
                        break
                    i+= disntance
    return False

def play():
    loop= True
    while loop:
        board= startedBoard[:]
        seeBoard(board)
        turn= 1
        while not tie(board):
            board= player(board, turn)
            turn*=-1
            seeBoard(board)
            if turn== 1:
                minMax(board, turn)
                print(move+1)
            if win(board):
                print("game over")
                break
        playAgain= input("Type 'yes' for playe again")
        if playAgain!= "yes":
            loop= False
play()
