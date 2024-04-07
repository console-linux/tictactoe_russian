import random

def drawBoard(board):
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print('---+---+---')
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print('---+---+---')
    print(f" {board[1]} | {board[2]} | {board[3]} ")

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Вы выбираете X или O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # bo - board le - letter
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))

def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Ваш следующий ход? (1-9)')
        move =input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)

    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'


    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def getComputerMove_advanced(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'


    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    if isSpaceFree(board, 5):
        return 5

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

global AI_ADV_SCORE, AI_SCORE, DRAW_SCORE
AI_ADV_SCORE, AI_SCORE, DRAW_SCORE = 0, 0, 0
global n
n = 10000
if __name__ == 'main':

    for i in range(0, n+1):
        theBoard = [' '] * 10
        #playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        if turn == 'Человек':
            playerLetter, computerLetter = ['X', 'O']
        else:
            playerLetter, computerLetter = ['O', 'X']
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'Человек':
                move = getComputerMove_advanced(theBoard, playerLetter)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    AI_ADV_SCORE += 1
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        DRAW_SCORE += 1
                        break
                    else:
                        turn = 'Компьютер'
            else:
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)

                if isWinner(theBoard, computerLetter):
                    AI_SCORE += 1
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        DRAW_SCORE += 1

                        break
                    else:

                        turn = 'Человек'


    print(f'Advanced AI: {AI_ADV_SCORE}')
    print(f'Normal AI: {AI_SCORE}')
    print(f'Draw score: {DRAW_SCORE}')