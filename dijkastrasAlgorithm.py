'''

A -- 6 -- B \
|       / |  \
|      /  |   5 
|     /   |    \
1    2    2      C   
|   /     |    /
|  /      |   5
| /       |  / 
D -- 1 -- E /

'''
#Find the minimum distance from vertex A to vertex C

def dj():
    #Visit unvisited vertex with the smallest known distance from start (A-A = 0)
    