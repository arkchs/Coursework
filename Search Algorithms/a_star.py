from asyncio import timeout
from queue import PriorityQueue
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

#value of c is greater if the node is further from goal
#so we need to minimize this one
def heuristic_goal(node):
    c=0
    for i in range(len(node)):
        for j in range(len(node[0])):
            if goal[i][j]!=node[i][j]:
                c=c+1
    return c
#the value of c is greater if the node is close to start
#and minimize this one
def heuristic_start(node):
    c=0
    for i in range(len(node)):
        for j in range(len(node[0])):
            if start[i][j]==node[i][j]:
                c=c+1
    return c

def heuristic_astar(node):
    return heuristic_start(node)+heuristic_goal(node)

closed=[]

def isInList(node,list):
    for each in list:
        if node==each[1]:
            return True
    return False

def a_star():
    open=[]
    open.append((heuristic_astar(start),start))
    while open:
        front = open.pop(0)
        closed.append(front)
        if front[1] ==goal:
            print('goal found...')
            print(closed)
            return

        #else generate all the children and add to the queue
        else:
            list_succ = gen_succ(front[1])

            for each in list_succ:
                new_h=heuristic_astar(each)
                #check if each node of the successors list is int open and closed
                if not isInList(each,open) and not isInList(each,closed):
                    open.append((new_h,each))

                elif isInList(each,open):
                    #searching for the original node in open
                    h=(0,'')
                    for n in open:
                        if n[1]==each:
                            h=n
                    if new_h<h[0]:
                        open.remove(h)
                        open.append((new_h,each))
                        
                else:
                    #searching for the original node in closed
                    h=(0,'')
                    for n in closed:
                        if n[1]==each:
                            h=n
                    if new_h<h[0]:
                        closed.remove(h)
                        closed.append((new_h,each))
        open.sort()
        print(open)
        print(closed)
    print('the search was unsuccessful')

a_star()