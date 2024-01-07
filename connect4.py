startedBoard= [[0 for i in range(0, 7)] for i in range(0, 7)]

#El array de tablero maneja los valores 0 para vacio, y 1 y -1 para los jugadores o el programa
#The array board manega the values 0 for empty, and 1 and -1 for the players or the software
def seeBoard(board):
    print([str(j) for  j in range(1, 8)])
    lines= []
    for i in range(0, 7):
        line= []
        for j in range (0, 7):
            if board[j][i]== -1:
                line.append("x")
            elif board[j][i]== 1:
                line.append("o")
            else:
                line.append(" ")
        lines.append(line)
    lines.reverse()
    for line in lines:
        print(line)

def player(board, num= -1):
    fill= input("Select the column")
    if fill in "1234567":
        fill= int(fill)-1
        for i in range(0, 7):
            if board[fill][i]== 0:
                board[fill][i]= num
                return board
seeBoard(player(startedBoard))
