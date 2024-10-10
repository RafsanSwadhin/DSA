#iterative method
def bfs(graph,start):
    queue = [start]
    while queue:
        curr =queue.pop(0)
        print(curr)
        for val in graph[curr]:
            queue.append(val)
graph = {
    10:[20,30,40,50],
    20:[500],
    30:[100],
    40:[200],
    50:[60],
    60:[70],
    70: [],
    500:[1000],
    100:[],
    200:[],
    1000:[]
}
bfs(graph,10)