#recursive method
def dfs(graph,start):
    print(start)

    if len(graph[start]) == 0:
        return 
    for val in graph[start]:
        dfs(graph,val)

graph = {
    10:[20,30,40,50],
    20:[],
    30:[],
    40:[],
    50:[60],
    60:[70],
    70: []
}
dfs(graph,10)