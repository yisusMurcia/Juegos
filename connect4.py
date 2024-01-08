startedBoard= [0 for i in range(0, 49)]

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