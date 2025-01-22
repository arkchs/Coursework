import copy
from queue import PriorityQueue

start=[[2,0,3],
       [1,8,4],
       [7,6,5]]

goal=[[1,2,3],
       [8,0,4],
       [7,6,5]]

def _findZeroIndex(node):
    for i in range(len(node[0])):
        for j in range(len(node)):
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
    

def heuristic(node):
    c=0
    for i in range(len(node)):
        for j in range(len(node[0])):
            if goal[i][j]!=node[i][j]:
                c=c+1
    return c


closed=[]

def shc():
    open=(heuristic(start),start)
    while True:
        #check if the goal state is found
        (next_h,next)=open
        closed.append((next_h,next))
        if next_h==0 and next==goal:
            print('goal state is found')
            print(closed)
            return
        #if the current node is not the goal state then find the next node to generate and continue
        else:
            flag=0
            list_succ=gen_succ(next)
            min=(next_h,next)
            for each in list_succ:
                each_h=heuristic(each)
                if each_h < min[0]:
                    min=(each_h,each)
                    flag=1 # this symbolizes that a better value was found
            open=min
            #if we can't find a better value in the entirety of the successors then
            if flag==0:
                print('unsuccessful search...')
                return


shc()