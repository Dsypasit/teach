board = ['-' for i in range(9)]
def boardShow():
    print(board[0]+'|'+board[1]+'|'+board[2])
    print(board[3]+'|'+board[4]+'|'+board[5])
    print(board[6]+'|'+board[7]+'|'+board[8])

def selectXo():
    run = True
    while run:
        n=input('Select x or o : ')
        if n in ['x','o']:
            if n == 'o':
                run = False
                return 'o','x'
            else:
                run = False
                return 'x','o'
        else:
            print('pleas select between x or o')

def addBoard(position, board, symbol):
    for i in range(len(board)):
        if i == position:
            board[i] = symbol

def win(b,symbol):
    if b[0]==symbol and b[1]==symbol and b[2]==symbol:
        return True
    elif b[3]==symbol and b[4]==symbol and b[5]==symbol:
        return True
    elif b[6]==symbol and b[7]==symbol and b[8]==symbol:
        return True
    elif b[0]==symbol and b[3]==symbol and b[6]==symbol:
        return True
    elif b[1]==symbol and b[4]==symbol and b[7]==symbol:
        return True
    elif b[2]==symbol and b[5]==symbol and b[8]==symbol:
        return True
    elif b[0]==symbol and b[4]==symbol and b[8]==symbol:
        return True
    elif b[2]==symbol and b[4]==symbol and b[6]==symbol:
        return True
    else:
        return False

def isBlank(pos,board):
    return board[pos]=='-'

def isFull(board):
    if board.count('-')>0:
        return False
    else:
        return True

def playerMove(symbol,board):
    run = True
    while run:
        move=input("Please put you position your want : ")
        try:
            move = int(move)
            if move>0 and move<10:
                if isBlank(move-1,board):
                    addBoard(move-1,board,symbol)
                    run = False
                else:
                    print("sorry, It's full.")
            else:
                print("please select between 1 to 9")
        except:
            print('Please type a number')

def botMove(player,board):
    symbol=''
    if player=='o':
        symbol = 'x'
    elif player=='x':
        symbol = 'o'
    posible_pos=[x for x,letter in enumerate(board) if letter=='-']
    move = 0
    for let in [symbol,player]:
        for i in posible_pos:
            copy_board = board.copy()
            copy_board[i] = let
            if win(copy_board,let):
                move = i
                return move

    if 4 in posible_pos:
        move=4
        return move

    cornerOpen=[]
    for i in posible_pos:
        if i in [0,2,6,8]:
            cornerOpen.append(i)
            if len(cornerOpen)>0:
                move = selectRandom(cornerOpen)
                return move

    ceterOpen = []
    for i in posible_pos:
        if i in [1,3,5,7]:
            ceterOpen.append(i)
            if len(ceterOpen)>0:
                move = selectRandom(ceterOpen)
                return move

def selectRandom(posibleMove):
    import random
    n = len(posibleMove)
    r = random.randrange(0,n)
    return posibleMove[r]

def mainGame():
    print('Welcom to xo game -.-')
    player,bot = selectXo()
    run = True
    while not isFull(board):
        if not win(board,bot):
            playerMove(player,board)
            boardShow()
        else:
            print('You lose')
            break

        if isFull(board):
            if win(board,player):
                print('you win')
                break

        print('-'*7)

        if not win(board,player):
            addBoard(botMove(player,board),board,bot)
            boardShow()
        else:
            print('You win')
            break

        print('-'*5)

    if isFull(board):
        print('Draw')

    print('-'*5)

mainGame()
