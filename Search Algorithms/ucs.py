
adj_list = {
    'A': [('B', 2), ('C', 3),('D',2)],
    'B': [('F',1),('A',2)],
    'C': [('A',3),('E',2)],
    'D': [('A', 2),('A', 2)],
    'E': [('F',1),('C',2),('G',3)],
    'F': [('B',1),('E',1),('G',10)],
    'G': [('F',10),('E',3)]
}
goal='G'
open=[]
closed=[(0,'A','#')]


def isInList(node,list):
    for each in list:
        if each[1]==node:
            return True
    return False

def ucs(root):
    #if the root is the goal node
    if(root==goal):
        print('The root is the goal node')
        return
    #generate the nodes connected to the root and add them to the open list
    next_options = adj_list[root]
    for each in next_options:
        open.append((each[1],each[0],root))
    open.sort()

    #start the while until the open list is empty
    while open:
        #extract and remove the first value in the open list and then add it to the closed list
        current_node=open[0]
        open.remove(current_node)
        closed.append(current_node)
        #if the node == goal
        if(current_node[1]==goal):
            print(closed)
            return
        #else do the following
        else:
            #generate the new successors
            current_parent=current_node[1]
            next_options = adj_list[current_parent]
            for each in next_options:
                #if the node is completely new and not visited
                isOpen=isInList(each[0],open)
                isClosed=isInList(each[0],closed)
                if not isOpen and not isClosed:
                    new_cost=each[1]+current_node[0]
                    open.append((new_cost,each[0],current_parent))
                #else if the node is a part of the open list
                elif isOpen:
                    new_cost =each[1]+current_node[0]
                #where is the node in the open list
                    temp=(0,'','')
                    for node in open:
                        if node[1]==each[0]:
                            temp=node    
                    if new_cost<temp[0]:
                        open.remove(temp)
                        open.append((new_cost,each[0],current_parent))
                #else the node is a part of the closed list
                else:
                    new_cost =each[1]+current_node[0]
                    temp=(0,'','')
                    for node in closed:
                        if node[1]==each[0]:
                            temp=node    
                    if new_cost<temp[0]:
                        closed.remove(temp)
                        open.append((new_cost,each[0],current_parent))
            open.sort()

ucs('A')
#each=(node,cost)
#current_node(cost,node,parent)
#current_parent=node