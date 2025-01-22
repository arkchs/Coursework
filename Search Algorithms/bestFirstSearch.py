from queue import PriorityQueue
import copy

start=[[2,0,3],
       [1,8,4],
       [7,6,5]]

goal=[[1,2,3],
       [8,0,4],
       [7,6,5]]

def _findBlankIndex(node):
    for i in range(len(node)):
        for j in range(len(node[0])):
            if node[i][j]==0:
                return [i,j]
            
def gen_succ(node):

    
    [row,col]=_findBlankIndex(node)
    nr=len(node)
    nc=len(node)

    goLeft=copy.deepcopy(node)
    #make the blank go left
    if col-1>=0:
        goLeft[row][col]=goLeft[row][col-1]
        goLeft[row][col-1]=0


    goRight=copy.deepcopy(node)
    #make the blank go right
    if col+1<nc:
        goRight[row][col]=goRight[row][col+1]
        goRight[row][col+1]=0


    goUp=copy.deepcopy(node)
    #make the blank go up
    if row-1>=0:
        goUp[row][col]=goUp[row-1][col]
        goUp[row-1][col]=0


    goDown=copy.deepcopy(node)
    #make the blank go down
    if row+1<nr:
        goDown[row][col]=goDown[row+1][col]
        goDown[row+1][col]=0

    return [goLeft,goRight,goUp,goDown]

def heuristic(node):
    c=0
    for i in range(len(node)):
        for j in range(len(node[0])):
            if goal[i][j]!=node[i][j]:
                c=c+1
    return c

def findMin(list_succ):
    min=10000
    minNode=start
    for each in list_succ:
        h=heuristic(each)
        if min>h:
            min=h
            minNode=each
    return [min,minNode]


closed=[]

def bfs():
    queue=PriorityQueue()
    #input the source in the queue
    queue.put((heuristic(start),start))


    #generate the successors of this node
    list_succ=gen_succ(start)
    [min,minNode]=findMin(list_succ)
    #find the node in the successors generated that has the minimum value of the heuristic function
    queue.put((min,minNode))

    while not queue.empty():
        val=queue.get()
        closed.append(val[1])
        #check if the goal state is found
        if val[0]==0:
            print('goal state is found')
            print(closed)
            return
        #generate the successors
        else:
            [min,minNode]=findMin(gen_succ(val[1]))
            queue.put((min,minNode))
            print(closed,'\n')

bfs()