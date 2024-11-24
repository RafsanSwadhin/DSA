# def buildgraph(edges):
#     graph = {}
#     for edge in edges: 
#         pointA,pointB = edge
#         print("edge",edge)
#         print("A:",pointA,"B:",pointB)
#         if pointA not in graph:
#             graph[pointA] = []
#             print(graph)
#         if pointB not in graph:
#             graph[pointB] = []
#             print(graph)
#         graph[pointA].append(pointB)
#         #print(graph)
#         graph[pointB].append(pointA)
#         #print(graph)
#     return graph
    
# edges = [
#     ['i','j'],
#     ['k','i'],
#     ['m','k'],
#     ['k','l'],
#     ['o','n']
# ]

# print(buildgraph(edges))
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