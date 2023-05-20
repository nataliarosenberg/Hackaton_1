import random
def printboard(board):
    print("  ",end="")
    for e in range(len(board)):
            print(f" {e+1}",end="")
    print(" ")
    for i, row in enumerate(board):
        print(f'{"ABC"[i]} ',end="")
        for e in row:
            print(f"|{e}",end="")
        print("|")

def checkboard(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != " ": return row[0]
    columns = [[board[i][j] for i in range(len(board))] for j in range(len(board))]
    for c in columns: 
        if len(set(c)) == 1 and c[0] != " ": return c[0]
    diag1 = [board[i][i] for i in range(len(board))]
    if len(set(diag1)) == 1 and diag1[0] != " ": return diag1[0]
    diag2 = [board[len(board)-i-1][i] for i in range(len(board)-1,-1,-1)]
    if len(set(diag2)) == 1 and diag2[0] != " ": return diag2[0]
    return " "


def main():
    p1 = input("Please choose sign: ")
    p2= input("Please choose sign: ")
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    comp = input("Play with computer? y/n: ").lower() == 'y'
    printboard(board)
    currentplayer = p1
    for _ in range(9):
        if comp and currentplayer == p2:
            positions = []
            for y in range(len(board)):
                for x in range(len(board)):
                    if board[y][x] == " ": positions.append((y,x))
            y,x = random.choice(positions)
            board[y][x] = currentplayer
            currentplayer = p1
        else:
            while True:
                try:
                    position = input(f"Player {currentplayer} input: ").lower()
                    ypos,xpos = "abc".index(position[0]), int(position[1])-1
                except Exception:continue
                if board[ypos][xpos] == " ":
                    board[ypos][xpos] = currentplayer
                    currentplayer = p1 if currentplayer == p2 else p2
                    break
                else: print('position already taken')
        printboard(board)
        if checkboard(board) != " ": 
            print(f"Player {checkboard(board)} wins!")
            return

main()