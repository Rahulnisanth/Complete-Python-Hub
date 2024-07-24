# COUNT THE NO. OF. TRIANGLES IN THE GIVEN GRAPH :
from collections import defaultdict

def multiply(A, B, C):
	global V
	for i in range(V):
		for j in range(V):
			C[i][j] = 0
			for k in range(V):
				C[i][j] += A[i][k] * B[k][j]

def getTrace(graph):
	global V
	trace = 0
	for i in range(V):
		trace += graph[i][i] 
	return trace

def triangleInGraph(graph):
	global V
	aux2 = [[None] * V for i in range(V)]
	aux3 = [[None] * V for i in range(V)]

	for i in range(V):
		for j in range(V):
			aux2[i][j] = aux3[i][j] = 0
			
	multiply(graph, graph, aux2) 
	multiply(graph, aux2, aux3) 
	trace = getTrace(aux3) 
	return trace // 6


# DETECT CYCLE IN THE DIRECTED-GRAPH :
def detect_cycle(graph, V):
    def helper(node, visited, stack):
        visited.add(node)
        stack.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if helper(neighbor, visited, stack):
                    return True
            elif neighbor in stack:
                return True
        stack.remove(node)
        return False

    visited = set()
    stack = set()
    for node in range(V):
        if node not in visited:
            if helper(node, visited, stack):
                return "YES"
    return "NO"


# COUNT THE LARGEST CYCLE IN THE UN-DIRECTED & UN-WEIGHTED GRAPH :
from collections import defaultdict
def find_largest_cycle(graph, V):
    def dfs(v, visited, stack, cycle_lengths):
        visited.add(v)
        stack.append(v)
        for neighbor in graph[v]:
            if neighbor in stack:
                start_idx = stack.index(neighbor)
                length = len(stack) - start_idx
                cycle_lengths.append(length)
            elif neighbor not in visited:
                dfs(neighbor, v, visited, stack, cycle_lengths)
        stack.pop()
    
    visited = set()
    cycle_lengths = []
    for v in range(1, V + 1):
        if v not in visited:
            dfs(v, visited, [], cycle_lengths)
    return max(cycle_lengths)

# Input drive :
V = int(input())
E = int(input())
graph = defaultdict(list)
for _ in range(E):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)
# Answer :
print(find_largest_cycle(graph, V))
