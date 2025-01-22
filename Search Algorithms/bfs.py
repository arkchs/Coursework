import copy

start=[[2,0,3],
       [1,8,4],
       [7,6,5]]

goal=[[2,8,3],
       [1,6,4],
       [7,5,0]]

def _findZeroIndex(node):
    for i in range(len(node)):
        for j in range(len(node[0])):
            if node[i][j]==0:
                return [i,j]
            

def gen_succ(node):

    [row,col]=_findZeroIndex(node)
    list_of_succ=[]
    goLeft=copy.deepcopy(node)
    if col-1>=0:
        goLeft[row][col]=goLeft[row][col-1]
        goLeft[row][col-1]=0
    if goLeft!=node:
        list_of_succ.append(goLeft)
        
    goRight=copy.deepcopy(node)
    if col+1<len(node[0]):
        goRight[row][col]=goRight[row][col+1]
        goRight[row][col+1]=0
    if goRight!=node:
        list_of_succ.append(goRight)
        
    goUp=copy.deepcopy(node)
    if row-1>=0:
        goUp[row][col]=goUp[row-1][col]
        goUp[row-1][col]=0
    if goUp!=node:
        list_of_succ.append(goUp)
        
    goDown=copy.deepcopy(node)
    if row+1<len(node):
        goDown[row][col]=goDown[row+1][col]
        goDown[row+1][col]=0
    if goDown!=node:
        list_of_succ.append(goDown)

    return list_of_succ

def _isInList(node,visited):
    for each in visited:
        if each==node:
            return True
    return False

def bfs():
    q=[]
    q.append(start)
    visited=[]
    while len(q)!=0:
        front = q.pop(0)
        #if the node matches the goal node
        if front ==goal:
            print(front)
            print('found the goal state')
            return
        #else generate all the successors that are possible and then add them to the queue one by one
        else:
            visited.append(front)
            #generate it's successors
            list_of_succ = gen_succ(front)
            for eachNode in list_of_succ:
                if not _isInList(eachNode,visited):
                    q.append(eachNode)
                    print(eachNode)
        print('\n')
bfs()