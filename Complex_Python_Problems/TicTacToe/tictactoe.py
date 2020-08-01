board=[' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    
def isWinner(bo,le):
    return ((bo[7]==le and bo[8]==le and bo[9]==le) or
            (bo[4]==le and bo[5]==le and bo[6]==le) or
            (bo[1]==le and bo[2]==le and bo[3]==le) or
            (bo[7]==le and bo[4]==le and bo[1]==le) or
            (bo[8]==le and bo[5]==le and bo[2]==le) or
            (bo[9]==le and bo[6]==le and bo[3]==le) or
             (bo[1]==le and bo[5]==le and bo[9]==le) or
            (bo[7]==le and bo[5]==le and bo[3]==le))
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
def playerMove():
    run = True
    while run:
        move = input('select position for X(1-9): ')
        try:
            move = int(move)
            if(move > 0 and move < 10):
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('sorry,this place is occupied')
            else:
                print('Please type a no. within range')
        except:
            print('Please type a no.!')
def compMove():
    possibleMoves = [x for x,letter in enumerate(board) if letter==' ' and x!=0]
    move = 0
    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move=selectRandom(cornersOpen)
        return move
    if 5 in possibleMoves:
        move=5
        return move
    edgesOpen=[]
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen)>0:
        move=selectRandom(edgesOpen)
    return move
def selectRandom(li):
    import random
    ln=len(li)
    r=random.randrange(0,ln)
    return li[r]

def main():
    print('Welcom to ticTactoe ,Enter no. b/w (1-9): ')
    printBoard(board)
    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('sorry,i won')
            break

        if not(isWinner(board, 'X')):
            move=compMove()
            if move == 0:
                print('Tie game')
            else:
                insertLetter('O', move)
                print('Computer placed O in', move, ':')
                printBoard(board)
        else:
            print('Good job,you won')
            break
    if isBoardFull(board):
        print('Tie game')

main()    
        
            
  
                    
