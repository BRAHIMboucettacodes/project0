"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xcounter=0
    ocounter=0
    for cell in board:
        xcounter+=cell.count(X)
        ocounter+=cell.count(O)
    return X if(xcounter<=ocounter) else O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_available=set()
    for i,row in enumerate(board):
        for j,col in enumerate (row):
            if board[i][j] == EMPTY:
                actions_available.add((i,j))
    return actions_available
 
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j=action
    newboard=deepcopy(board)
    curentplayer=player(newboard)
    if newboard[i][j] is not EMPTY:
        raise Exception("not a valid action")
    else:
        newboard[i][j]=curentplayer
    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row.count(X)==3:
            return X
        elif row.count(O)==3:
            return O
        
    col=[]
    for i in range(len(board)):
        col.append([row[i] for row in board])
    for j in col:
        if j.count(X)==3:
            return X
        elif j.count(O)==3:
            return O 
    

    # None | Todo: Modify to simplify terminal
    
     
    diag=[]
    tdiag=[]
    for i,row in enumerate(board):
            for j,col in enumerate (row):
                if i==j:
                    diag.append(board[i][j])
                if (i==0 and j==2) or (i==1 and j==1)or (i==2 and j==0):
                    tdiag.append(board[i][j])
    if diag.count(X)==3:
        return X
    elif diag.count(O)==3:
    
        return O
    if tdiag.count(X)==3:
        return X
    elif tdiag.count(O)==3:
        return O
    else:    
        return None



                


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board) is not None:
        return True
    else:
        for row in board:
            if EMPTY in row:
                return False
        return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    a=-math.inf
    b=math.inf
    def max_value(board,a,b):
        if terminal(board):
            return utility(board)
        v=-math.inf
        for action in actions(board):
            v=max(v,min_value(result(board,action),a,b))
            if v >= b:
              return v
            a=max(a,v)
        return v
    def min_value(board,a,b):
        if terminal(board):
            return utility(board)
        v=math.inf
        for action in actions(board):
            v=min(v,max_value(result(board,action),a,b))
            if v <= a:
              return v
            b=min(b,v)
        return v
    if player(board) == X:
        maxi = -math.inf
        for action in actions(board):
            value = min_value(result(board, action),a,b)
            if value > maxi:
                maxi = value
                optimal_solution = action
    else:
        mini = math.inf
        for action in actions(board):
            value = max_value(result(board, action),a,b)
            if value < mini:
                mini = value
                optimal_solution = action
 
    return optimal_solution