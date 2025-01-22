import copy

start=[[2,0,3],
       [1,8,4],
       [7,6,5]]

goal=[[1,2,3],
       [8,0,4],
       [7,6,5]]

def _findZeroIndex(node):
    for i in range(len(node)):
        for j in range(len(node[0])):
            if node[i][j]==0:
                return [i,j]
            

def gen_succ(node):

    [row,col]=_findZeroIndex(node)
    list_of_succ=[]
    goDown=copy.deepcopy(node)
    if row+1<len(node):
        goDown[row][col]=goDown[row+1][col]
        goDown[row+1][col]=0
    if goDown!=node:
        list_of_succ.append(goDown)

    goUp=copy.deepcopy(node)
    if row-1>=0:
        goUp[row][col]=goUp[row-1][col]
        goUp[row-1][col]=0
    if goUp!=node:
        list_of_succ.append(goUp) 

    goRight=copy.deepcopy(node)
    if col+1<len(node[0]):
        goRight[row][col]=goRight[row][col+1]
        goRight[row][col+1]=0
    if goRight!=node:
        list_of_succ.append(goRight)

    goLeft=copy.deepcopy(node)
    if col-1>=0:
        goLeft[row][col]=goLeft[row][col-1]
        goLeft[row][col-1]=0
    if goLeft!=node:
        list_of_succ.append(goLeft)
    return list_of_succ

def _isInList(node,visited):
    for each in visited:
        if each==node:
            return True
    return False

def dls(limiter):
    s=[]
    s.append(start)
    visited=[]
    while limiter!=0 and len(s)!=0:
        front = s.pop(-1)
        #if the node matches the goal node
        if front ==goal:
            print(front)
            print('found the goal state')
            return True
        #else generate all the successors that are possible and then add them to the queue one by one
        else:
            visited.append(front)
            #generate it's successors
            list_of_succ = gen_succ(front)
            for eachNode in list_of_succ:
                if not _isInList(eachNode,visited):
                    s.append(eachNode)
                    print(eachNode)
        limiter=limiter-1
        print('limiter',limiter)
    print('goal state not found.... please increase the depth limiter')
    return False

dls(4)