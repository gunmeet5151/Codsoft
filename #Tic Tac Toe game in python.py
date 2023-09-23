board = [' ' for _ in range(9)]  # Updated to a 9-element board

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    
def isWinner(bo, le):
    return (bo[6] == le and bo[7] == le and bo[8] == le) or \
           (bo[3] == le and bo[4] == le and bo[5] == le) or \
           (bo[0] == le and bo[1] == le and bo[2] == le) or \
           (bo[0] == le and bo[3] == le and bo[6] == le) or \
           (bo[1] == le and bo[4] == le and bo[7] == le) or \
           (bo[2] == le and bo[5] == le and bo[8] == le) or \
           (bo[0] == le and bo[4] == le and bo[8] == le) or \
           (bo[2] == le and bo[4] == le and bo[6] == le)

def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move - 1):  # Adjust position to match list indexing
                    run = False
                    insertLetter('X', move - 1)  # Adjust position to match list indexing
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except ValueError:
            print('Please type a number!')

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ']
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = [i for i in possibleMoves if i in [0, 2, 6, 8]]

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 4 in possibleMoves:
        move = 4

    edgesOpen = [i for i in possibleMoves if i in [1, 3, 5, 7]]

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(ln)
    return li[r]

def isBoardFull(board):
    return ' ' not in board

def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not isBoardFull(board):
        if not isWinner(board, 'O'):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not isWinner(board, 'X'):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move + 1, ':')  # Adjust position for user input
                printBoard(board)
        else:
            print('X\'s won this time! Good Job!')
            break

    if isBoardFull(board):
        print('Tie Game!')

while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower() == 'yes':
        board = [' ' for _ in range(9)]  # Reset the board for a new game
        print('-----------------------------------')
        main()
    else:
        break
