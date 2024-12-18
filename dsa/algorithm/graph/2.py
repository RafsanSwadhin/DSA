#user input
def buildgraph(edges):
    graph = {}
    for edge in edges: 
        pointA,pointB = edge
        if pointA not in graph:
            graph[pointA] = []
        if pointB not in graph:
            graph[pointB] = []
        graph[pointA].append(pointB)
        graph[pointB].append(pointA)
    return graph
    
# edges = [
#     ['i','j'],
#     ['k','i'],
#     ['m','k'],
#     ['k','l'],
#     ['o','n']
# ]
n = 5
edges = []
for i in  range(n):
    edges.append(input().split())
print(buildgraph(edges))