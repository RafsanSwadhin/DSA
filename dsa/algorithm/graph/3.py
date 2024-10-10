#iterative mathod
def dfs(graph,start):
    stack = [start]
    while stack:
        curr = stack.pop()
        print(curr)
        for val in graph[curr]:
            stack.append(val)

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