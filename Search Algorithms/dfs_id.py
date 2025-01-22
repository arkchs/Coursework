import dfs_limited

def dfs_id():
    level=2
    res=dfs_limited.dfs(level)
    while True:
        if res:
            print('goal state was found at the depth level ',level)
            return
        else:
            level=level+1
            res=dfs_limited.dls(level)
dfs_id()