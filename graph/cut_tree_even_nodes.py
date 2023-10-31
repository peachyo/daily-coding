from collections import defaultdict


# O(n) time and space
# cut edge where a node has odd number of descendants

def traverse(graph, curr, result):
    descendants = 0

    for child in graph[curr]:
        num_nodes, result = traverse(graph, child, result)
        result[child] += num_nodes - 1
        descendants += num_nodes
    return descendants + 1, result

def max_edges(graph):
    start = list(graph)[0]
    vertices = defaultdict(int)

    _, descendants = traverse(graph, start, vertices)

    return len([val for val in descendants.values() if val % 2 == 1])
